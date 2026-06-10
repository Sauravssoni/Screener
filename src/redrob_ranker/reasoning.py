def generate_reasoning(candidate, features, traps):
    prof = candidate.get('profile', {})
    title = prof.get('current_title', 'Engineer')
    yoe = prof.get('years_of_experience', 0)
    
    parts = []
    
    # Technical reasoning
    if features['core_ai_count'] > 0:
        parts.append(f"{title} with {yoe} yrs; {features['core_ai_count']} AI core skills;")
    else:
        parts.append(f"{title} with {yoe} yrs;")
        
    if features['production_count'] > 0:
        parts.append("production experience;")
        
    if features['evaluation_count'] > 0:
        parts.append("evaluation expertise;")
        
    if traps > 0:
        parts.append(f"flagged {traps} risk(s);")
        
    parts.append(f"response rate {features['response_rate']:.2f}.")
    
    return " ".join(parts)
