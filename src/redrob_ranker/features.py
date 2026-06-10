from src.redrob_ranker.text import count_terms, normalize_text

CORE_AI_TERMS = [
    "embeddings",
    "vector search",
    "semantic search",
    "hybrid search",
    "retrieval",
    "ranking",
    "recommender systems",
    "search relevance",
    "information retrieval",
    "faiss",
    "milvus",
    "qdrant",
    "pinecone",
    "weaviate",
    "elasticsearch",
    "opensearch",
    "bm25",
    "ann",
    "hnsw",
    "rag",
    "sentence-transformers",
    "bge",
    "e5",
    "llm ranking",
    "learning-to-rank",
]

PRODUCTION_TERMS = [
    "production",
    "deployed",
    "real users",
    "latency",
    "monitoring",
    "online",
    "a/b testing",
    "index refresh",
    "serving",
    "mlops",
    "on-call",
    "feature pipeline",
    "quality regression",
    "model deployment",
]

EVALUATION_TERMS = [
    "ndcg",
    "map",
    "mrr",
    "ranking metrics",
    "offline benchmark",
    "online experiment",
    "a/b test",
    "relevance labels",
    "recruiter feedback",
    "click model",
    "evaluation framework",
]

PYTHON_SYSTEMS_TERMS = [
    "python",
    "fastapi",
    "pandas",
    "numpy",
    "pytorch",
    "scikit-learn",
    "airflow",
    "spark",
    "kafka",
    "docker",
    "kubernetes",
    "aws",
    "gcp",
    "distributed systems",
    "large-scale inference",
    "batch pipelines",
]

NEGATIVE_TERMS = ["research-only", "academic lab", "tutorial", "demo", "prototype", "kaggle"]


def extract_features(candidate):
    prof = candidate.get("profile", {})
    history = candidate.get("career_history", [])
    skills = candidate.get("skills", [])
    signals = candidate.get("redrob_signals", {})

    # Text pool
    career_texts = [h.get("description", "") for h in history if h.get("description")]
    # career_titles = [h.get('title', '') for h in history]
    full_text = " ".join(career_texts) + " " + prof.get("summary", "") + " " + prof.get("headline", "")

    # Hard skills from list
    skill_names = [s.get("name", "").lower() for s in skills]

    features = {}

    # 1. Core AI Retrieval
    features["core_ai_count"] = count_terms(full_text, CORE_AI_TERMS) + sum(
        1 for s in skill_names if any(t in s for t in CORE_AI_TERMS)
    )

    # 2. Production
    features["production_count"] = count_terms(full_text, PRODUCTION_TERMS)

    # 3. Evaluation
    features["evaluation_count"] = count_terms(full_text, EVALUATION_TERMS)

    # 4. Python/Systems
    features["python_systems_count"] = count_terms(full_text, PYTHON_SYSTEMS_TERMS) + sum(
        1 for s in skill_names if any(t in s for t in PYTHON_SYSTEMS_TERMS)
    )

    # 5. Career Shape
    yoe = prof.get("years_of_experience", 0)
    features["yoe_ideal"] = 1 if 4 <= yoe <= 12 else 0
    features["yoe_too_junior"] = 1 if yoe < 3 else 0
    features["yoe_too_senior"] = 1 if yoe > 15 else 0

    curr_title = normalize_text(prof.get("current_title", ""))
    features["is_manager_only"] = (
        1 if "manager" in curr_title and not any(t in curr_title for t in ["engineer", "data", "applied"]) else 0
    )
    features["is_research_only"] = count_terms(full_text, NEGATIVE_TERMS)

    # 6. Behavioral
    features["profile_completeness"] = signals.get("profile_completeness_score", 0) / 100.0
    features["response_rate"] = signals.get("recruiter_response_rate", 0)
    features["github_active"] = 1 if signals.get("github_activity_score", -1) > 10 else 0
    features["open_to_work"] = 1 if signals.get("open_to_work_flag", False) else 0

    # 7. Location
    loc = normalize_text(prof.get("location", ""))
    features["ideal_location"] = (
        1 if any(city in loc for city in ["pune", "noida", "delhi", "gurgaon", "bangalore", "bengaluru"]) else 0
    )
    features["willing_to_relocate"] = 1 if signals.get("willing_to_relocate", False) else 0

    return features


def detect_traps(candidate, features):
    traps = 0
    # 1. Expert skills with tiny duration
    skills = candidate.get("skills", [])
    for s in skills:
        if s.get("proficiency") == "expert" and s.get("duration_months", 0) < 6:
            traps += 1

    # 2. Many core AI skills but zero production verbs
    if features["core_ai_count"] > 5 and features["production_count"] == 0:
        traps += 2

    # 3. YOE inconsistency (sum of career vs declared YOE)
    history = candidate.get("career_history", [])
    sum_months = sum(h.get("duration_months", 0) for h in history)
    declared_months = candidate.get("profile", {}).get("years_of_experience", 0) * 12
    if abs(sum_months - declared_months) > 24:  # Allowing 2 years gap
        traps += 1

    # 4. Bad availability
    signals = candidate.get("redrob_signals", {})
    if signals.get("notice_period_days", 0) > 60 and not signals.get("open_to_work_flag", False):
        traps += 1

    return traps
