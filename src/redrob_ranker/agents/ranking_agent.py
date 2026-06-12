import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from src.redrob_ranker.reasoning import generate_reasoning


def compute_career_relevance(candidate):
    # Recency-weighted AI experience
    history = candidate.get("career_history", [])
    if not history:
        return 0.0

    score = 0.0
    weight = 1.0
    # Assuming history is sorted by recency
    for role in history[:3]:
        desc = role.get("description", "").lower()
        title = role.get("title", "").lower()
        if any(
            kw in title or kw in desc
            for kw in ["machine learning", "ai", "data scientist", "nlp", "llm", "recommendation"]
        ):
            score += weight
        weight *= 0.6
    return min(score, 1.0)


def compute_skill_trust(candidate):
    skills = candidate.get("skills", [])
    if not skills:
        return 0.0

    trust_score = 0.0
    for s in skills:
        # Higher score if duration > 24 months, high proficiency, or high endorsements
        score = 0.1
        if s.get("duration_months", 0) > 24:
            score += 0.2
        if s.get("proficiency") in ["expert", "advanced"]:
            score += 0.2
        if s.get("endorsements", 0) > 5:
            score += 0.1
        trust_score += score

    return min(trust_score / max(len(skills), 1), 1.0) * 2.0  # normalize


def rank_candidates(candidates_with_context):
    """
    Ranks candidates using deterministic multi-signal scoring logic and RRF.
    candidates_with_context is a list of tuples: (candidate_dict, features, traps, evidence)
    """

    # 1. Prepare corpus for Lexical/TF-IDF Scoring
    corpus = []
    for c, f, t, e in candidates_with_context:
        prof = c.get("profile", {})
        history = c.get("career_history", [])
        career_texts = [h.get("description", "") for h in history if h.get("description")]
        skills_text = " ".join([s.get("name", "") for s in c.get("skills", [])])
        full_text = (
            " ".join(career_texts) + " " + prof.get("summary", "") + " " + prof.get("headline", "") + " " + skills_text
        )
        corpus.append(full_text)

    jd_query = "Senior AI Engineer embeddings vector search semantic search information retrieval ranking recommendation systems LLM RAG fine-tuning NLP transformers production MLOps pipeline scalability"

    vectorizer = TfidfVectorizer(stop_words="english", max_features=5000, ngram_range=(1, 2))
    corpus.append(jd_query)

    tfidf_matrix = vectorizer.fit_transform(corpus)
    query_vec = tfidf_matrix[-1]
    candidate_vecs = tfidf_matrix[:-1]

    # Module 2: Lexical/TF-IDF recall score
    semantic_scores = cosine_similarity(query_vec, candidate_vecs).flatten()

    structured_scores = []

    for i, (candidate, features, traps, evidence) in enumerate(candidates_with_context):
        # Module 3: Structured AI skill score
        core_ai = min(features["core_ai_count"] / 5.0, 1.0)

        # Module 4: Skill trust score
        trust_score = min(compute_skill_trust(candidate), 1.0)

        # Module 5: Career relevance
        career_rel = compute_career_relevance(candidate)

        # Module 6: Production/MLOps
        prod = min(features["production_count"] / 3.0, 1.0)

        # Module 7: Evaluation/Experimentation
        eval_score = min(features["evaluation_count"] / 2.0, 1.0)

        # Module 8: Behavioral availability
        behavioral = (
            features["profile_completeness"] * 0.4 + features["response_rate"] * 0.4 + features["open_to_work"] * 0.2
        )

        # Module 9: Location score
        location = max(features["ideal_location"], features["willing_to_relocate"] * 0.5)

        # Weighted Fusion
        struct_score = (
            0.25 * core_ai
            + 0.15 * trust_score
            + 0.15 * career_rel
            + 0.15 * prod
            + 0.10 * eval_score
            + 0.10 * behavioral
            + 0.10 * location
        )

        # Module 10: Risk / Honeypot score (applied as deduction)
        struct_score = max(struct_score - (traps * 0.15), 0.0)

        # Module 1: Hard Disqualifier
        prof = candidate.get("profile", {})
        title = prof.get("current_title", "").lower()
        yoe = prof.get("years_of_experience", 0)

        if features["is_non_tech"] or features["is_manager_only"] or features["is_research_only"]:
            if features["core_ai_count"] < 2:
                struct_score = 0.0

        if yoe < 3:
            struct_score = 0.0

        if (
            "customer support" in title
            or "accountant" in title
            or "civil engineer" in title
            or "operations manager" in title
            or "content writer" in title
            or "hr" in title
            or "sales" in title
            or "marketing" in title
            or "teacher" in title
            or "recruiter" in title
        ):
            struct_score = 0.0

        structured_scores.append(struct_score)

    # Reciprocal Rank Fusion (RRF)
    k = 60
    semantic_ranks = {idx: rank for rank, idx in enumerate(np.argsort(-semantic_scores))}
    struct_ranks = {idx: rank for rank, idx in enumerate(np.argsort(-np.array(structured_scores)))}

    scored = []
    for i, (candidate, features, traps, evidence) in enumerate(candidates_with_context):
        # Calculate RRF final score
        rrf_score = (1.0 / (k + semantic_ranks[i])) + (1.0 / (k + struct_ranks[i]))

        if structured_scores[i] == 0.0:
            rrf_score = 0.0

        candidate["final_score"] = round(rrf_score, 4)
        candidate["semantic_score"] = float(semantic_scores[i])
        candidate["struct_score"] = float(structured_scores[i])
        candidate["features"] = features
        candidate["traps"] = traps
        candidate["evidence"] = evidence

        candidate["reasoning"] = generate_reasoning(candidate, features, traps, evidence)
        scored.append(candidate)

    # Sort strictly by score descending, then candidate_id ascending
    return sorted(scored, key=lambda x: (-x["final_score"], x["candidate_id"]))
