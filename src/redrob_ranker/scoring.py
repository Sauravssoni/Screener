from src.redrob_ranker.features import extract_features, detect_traps
from src.redrob_ranker.reasoning import generate_reasoning
from src.redrob_ranker.io import stream_candidates

def score_candidates(filepath):
    scored = []
    
    for candidate in stream_candidates(filepath):
        features = extract_features(candidate)
        traps = detect_traps(candidate, features)
        
        # Scoring logic based on weights
        # Normalize counts by capping
        core_ai = min(features['core_ai_count'] / 5.0, 1.0)
        prod = min(features['production_count'] / 3.0, 1.0)
        eval_score = min(features['evaluation_count'] / 2.0, 1.0)
        python = min(features['python_systems_count'] / 4.0, 1.0)
        
        career_shape = features['yoe_ideal'] - (features['yoe_too_junior'] * 0.5) - (features['is_manager_only'] * 0.8) - (features['is_research_only'] * 0.3)
        career_shape = max(career_shape, 0)
        
        behavioral = (features['profile_completeness'] * 0.4 + 
                      features['response_rate'] * 0.4 + 
                      features['open_to_work'] * 0.2)
                      
        location = max(features['ideal_location'], features['willing_to_relocate'] * 0.5)
        
        final_score = (
            0.35 * core_ai +
            0.18 * prod +
            0.14 * eval_score +
            0.10 * python +
            0.08 * career_shape +
            0.07 * behavioral +
            0.04 * location
        ) - (traps * 0.15)
        
        final_score = max(final_score, 0)
        
        # We need final score, reasoning
        candidate['final_score'] = final_score
        candidate['features'] = features
        candidate['traps'] = traps
        
        candidate['reasoning'] = generate_reasoning(candidate, features, traps)
        
        scored.append(candidate)
        
    return scored
