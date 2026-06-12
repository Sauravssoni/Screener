import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from src.redrob_ranker.reasoning import generate_reasoning

def rank_candidates(candidates_with_context):
    """
    Ranks candidates using deterministic multi-signal scoring logic and RRF.
    candidates_with_context is a list of tuples: (candidate_dict, features, traps, evidence)
    """
    
    # 1. Prepare corpus for Semantic Scoring (TF-IDF)
    corpus = []
    for c, f, t, e in candidates_with_context:
        prof = c.get("profile", {})
        history = c.get("career_history", [])
        career_texts = [h.get("description", "") for h in history if h.get("description")]
        skills_text = " ".join([s.get("name", "") for s in c.get("skills", [])])
        full_text = " ".join(career_texts) + " " + prof.get("summary", "") + " " + prof.get("headline", "") + " " + skills_text
        corpus.append(full_text)
        
    jd_query = "Senior AI Engineer embeddings vector search semantic search information retrieval ranking recommendation systems LLM RAG fine-tuning NLP transformers production MLOps"
    
    vectorizer = TfidfVectorizer(stop_words='english', max_features=5000, ngram_range=(1, 2))
    # We add jd_query to the end to fit the vocabulary easily
    corpus.append(jd_query)
    
    tfidf_matrix = vectorizer.fit_transform(corpus)
    query_vec = tfidf_matrix[-1]
    candidate_vecs = tfidf_matrix[:-1]
    
    # Compute semantic similarity scores
    semantic_scores = cosine_similarity(query_vec, candidate_vecs).flatten()
    
    # 2. Compute Structured Scores
    structured_scores = []
    
    for i, (candidate, features, traps, evidence) in enumerate(candidates_with_context):
        core_ai = min(features["core_ai_count"] / 4.0, 1.0)
        prod = min(features["production_count"] / 3.0, 1.0)
        eval_score = min(features["evaluation_count"] / 2.0, 1.0)
        python = min(features["python_systems_count"] / 4.0, 1.0)

        # Career recency & YOE logic
        yoe_score = features["yoe_ideal"] - (features["yoe_too_junior"] * 0.5)
        yoe_score = max(yoe_score, 0)

        # Behavioral & Risk signals
        behavioral = (
            features["profile_completeness"] * 0.4 + features["response_rate"] * 0.4 + features["open_to_work"] * 0.2
        )
        location = max(features["ideal_location"], features["willing_to_relocate"] * 0.5)

        struct_score = (
            0.35 * core_ai
            + 0.20 * prod
            + 0.15 * eval_score
            + 0.10 * python
            + 0.10 * yoe_score
            + 0.05 * behavioral
            + 0.05 * location
        )

        # Hard Penalties
        if features["is_non_tech"] and features["core_ai_count"] < 2:
            struct_score = 0.0
        elif features["is_research_only"] and features["production_count"] == 0:
            struct_score = 0.0
        elif features["is_manager_only"] and features["python_systems_count"] == 0:
            struct_score = 0.0
        elif features["is_prompt_only"]:
            struct_score *= 0.5
        elif features["yoe_too_junior"] and features["core_ai_count"] < 3:
            struct_score *= 0.5

        struct_score = max(struct_score - (traps * 0.15), 0.0)
        structured_scores.append(struct_score)
        
    # 3. Reciprocal Rank Fusion (RRF)
    # RRF Score = 1 / (k + rank)
    k = 60
    
    # Get ranks for semantic
    semantic_ranks = {idx: rank for rank, idx in enumerate(np.argsort(-semantic_scores))}
    # Get ranks for structured
    struct_ranks = {idx: rank for rank, idx in enumerate(np.argsort(-np.array(structured_scores)))}
    
    scored = []
    for i, (candidate, features, traps, evidence) in enumerate(candidates_with_context):
        # Calculate RRF final score
        rrf_score = (1.0 / (k + semantic_ranks[i])) + (1.0 / (k + struct_ranks[i]))
        
        # Multiply by strict gating zero-outs
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

    # Sort strictly by score descending, then candidate_id ascending for deterministic tie break
    return sorted(scored, key=lambda x: (-x["final_score"], x["candidate_id"]))
