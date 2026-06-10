from src.redrob_ranker.features import count_terms, normalize_text, extract_features

def test_normalize():
    assert normalize_text("Hey-There") == "hey-there"

def test_features_extraction():
    candidate = {
        'profile': {'current_title': 'AI Engineer', 'years_of_experience': 5},
        'career_history': [{'description': 'used embeddings in production'}],
        'redrob_signals': {'open_to_work_flag': True}
    }
    feats = extract_features(candidate)
    
    assert feats['core_ai_count'] >= 1
    assert feats['production_count'] >= 1
    assert feats['open_to_work'] == 1
