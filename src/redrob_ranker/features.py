from src.redrob_ranker.text import normalize_text
import re

CORE_AI_TERMS = [
    "rag", "vector search", "semantic search", "hybrid search", "bm25",
    "faiss", "pinecone", "qdrant", "weaviate", "elasticsearch", "opensearch",
    "recommender systems", "recommendation systems", "learning-to-rank", "personalization", "relevance",
    "nlp", "transformers", "sentence-transformers", "hugging face", "fine-tuning", "peft", "qlora",
    "ranking", "retrieval", "llm", "large language models", "embedding", "embeddings",
    "milvus", "chroma", "cross-encoder", "bi-encoder", "langchain", "llamaindex"
]

PRODUCTION_TERMS = [
    "mlops", "deployment", "model serving", "latency", "monitoring", "pipelines",
    "docker", "kubernetes", "mlflow", "airflow", "fastapi", "production", "scale", "infrastructure"
]

EVALUATION_TERMS = [
    "ndcg", "map", "mrr", "precision", "recall", "offline benchmark", "a-b testing", "a/b testing",
    "experimentation", "feedback loops", "metrics", "eval", "hit rate"
]

PYTHON_SYSTEMS_TERMS = [
    "python", "sql", "spark", "kafka", "redis", "postgres", "snowflake", "dbt", "go", "c++"
]

NON_TECH_ROLES = ["customer support", "accountant", "civil engineer", "content writer", "operations manager", "hr", "sales", "marketing", "recruiter", "financial analyst", "teacher"]
MANAGER_ROLES = ["director", "vp", "manager", "head", "founder", "ceo", "cto"]
RESEARCH_TERMS = ["research-only", "academic lab", "tutorial", "student"]
PROMPT_TERMS = ["chatgpt", "prompt engineering", "wrapper"]

def extract_matched_terms(text, term_list):
    matched = []
    text_lower = normalize_text(text)
    for term in term_list:
        if term in text_lower:
            if re.search(r"\b" + re.escape(term) + r"\b", text_lower):
                matched.append(term)
    return matched

def extract_features(candidate):
    prof = candidate.get("profile", {})
    history = candidate.get("career_history", [])
    skills = candidate.get("skills", [])
    signals = candidate.get("redrob_signals", {})

    career_texts = [h.get("description", "") for h in history if h.get("description")]
    full_text = " ".join(career_texts) + " " + prof.get("summary", "") + " " + prof.get("headline", "")
    
    skill_names_lower = [s.get("name", "").lower() for s in skills]
    
    features = {}

    ai_matches = extract_matched_terms(full_text, CORE_AI_TERMS)
    for skill in skill_names_lower:
        for term in CORE_AI_TERMS:
            if term in skill and term not in ai_matches:
                ai_matches.append(term)
    features["core_ai_terms"] = ai_matches
    features["core_ai_count"] = len(ai_matches)

    prod_matches = extract_matched_terms(full_text, PRODUCTION_TERMS)
    features["production_terms"] = prod_matches
    features["production_count"] = len(prod_matches)

    eval_matches = extract_matched_terms(full_text, EVALUATION_TERMS)
    features["evaluation_terms"] = eval_matches
    features["evaluation_count"] = len(eval_matches)

    py_matches = extract_matched_terms(full_text, PYTHON_SYSTEMS_TERMS)
    for skill in skill_names_lower:
        for term in PYTHON_SYSTEMS_TERMS:
            if term in skill and term not in py_matches:
                py_matches.append(term)
    features["python_systems_terms"] = py_matches
    features["python_systems_count"] = len(py_matches)

    yoe = prof.get("years_of_experience", 0)
    features["yoe"] = yoe
    features["yoe_ideal"] = 1 if 4 <= yoe <= 12 else 0
    features["yoe_too_junior"] = 1 if yoe < 3 else 0
    
    curr_title = normalize_text(prof.get("current_title", ""))
    
    # Check negatives
    features["is_non_tech"] = 1 if any(t in curr_title for t in NON_TECH_ROLES) else 0
    features["is_manager_only"] = 1 if any(m in curr_title for m in MANAGER_ROLES) and not any(t in curr_title for t in ["engineer", "data", "applied", "ml", "scientist"]) else 0
    features["is_research_only"] = 1 if extract_matched_terms(full_text, RESEARCH_TERMS) else 0
    features["is_prompt_only"] = 1 if extract_matched_terms(full_text, PROMPT_TERMS) and features["core_ai_count"] < 2 else 0

    features["profile_completeness"] = signals.get("profile_completeness_score", 0) / 100.0
    features["response_rate"] = signals.get("recruiter_response_rate", 0)
    features["github_active"] = 1 if signals.get("github_activity_score", -1) > 10 else 0
    features["open_to_work"] = 1 if signals.get("open_to_work_flag", False) else 0

    loc = normalize_text(prof.get("location", ""))
    features["ideal_location"] = 1 if any(city in loc for city in ["pune", "noida", "delhi", "gurgaon", "bangalore", "bengaluru", "hyderabad", "chennai", "mumbai"]) else 0
    features["willing_to_relocate"] = 1 if signals.get("willing_to_relocate", False) else 0

    return features

def detect_traps(candidate, features):
    traps = 0
    skills = candidate.get("skills", [])
    for s in skills:
        if s.get("proficiency") == "expert" and s.get("duration_months", 0) < 6:
            traps += 1

    if features["core_ai_count"] > 5 and features["production_count"] == 0:
        traps += 1

    history = candidate.get("career_history", [])
    sum_months = sum(h.get("duration_months", 0) for h in history)
    declared_months = candidate.get("profile", {}).get("years_of_experience", 0) * 12
    if abs(sum_months - declared_months) > 36:
        traps += 1
        
    return traps
