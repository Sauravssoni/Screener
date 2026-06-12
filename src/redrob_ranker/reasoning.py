def generate_reasoning(candidate, features, traps, evidence=None):
    prof = candidate.get("profile", {})
    title = prof.get("current_title", "Unknown Role")
    yoe = prof.get("years_of_experience", 0)
    loc = prof.get("location", "Unknown Location")
    
    # Retrieve semantic scores
    sem_score = candidate.get("semantic_score", 0.0)
    
    parts = []
    
    parts.append(f"Candidate is a {title} with {yoe} YOE based in {loc}.")
    
    ai_terms = features.get("core_ai_terms", [])
    prod_terms = features.get("production_terms", [])
    eval_terms = features.get("evaluation_terms", [])
    
    if features["core_ai_count"] > 0:
        skills_str = f" (matched: {', '.join(ai_terms[:4])})" if ai_terms else ""
        parts.append(f"Strong AI indicators with {features['core_ai_count']} core terms{skills_str}.")
    
    if sem_score > 0.0:
        parts.append(f"JD Semantic Alignment Score: {sem_score:.3f}.")
        
    if features["production_count"] > 0:
        prod_str = f" (e.g., {', '.join(prod_terms[:3])})" if prod_terms else ""
        parts.append(f"Shows production shipping evidence{prod_str}.")

    if features["evaluation_count"] > 0:
        eval_str = f" ({', '.join(eval_terms[:2])})" if eval_terms else ""
        parts.append(f"Experience with ML evaluation metrics{eval_str}.")
        
    if features["python_systems_count"] > 0:
        parts.append(f"Mentions {features['python_systems_count']} python/systems keywords.")
        
    if features["response_rate"] > 0.5:
        parts.append(f"High Redrob response rate ({features['response_rate']:.0%}).")
        
    if traps > 0:
        parts.append(f"Note: {traps} risk flag(s) detected.")
        
    if features.get("is_prompt_only"):
        parts.append("Note: Heavy reliance on prompt-level skills without deep fundamentals.")
        
    # Add candidate ID to ensure uniqueness just in case 
    parts.append(f"[Ref: {candidate.get('candidate_id')}]")
        
    return " ".join(parts)
