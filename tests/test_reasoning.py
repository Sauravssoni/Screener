def test_generate_reasoning():
    from src.redrob_ranker.reasoning import generate_reasoning
    candidate = {
        'profile': {'current_title': 'AI Engineer', 'years_of_experience': 5},
        'redrob_signals': {}
    }
    features = {'core_ai_count': 3, 'production_count': 1, 'evaluation_count': 0, 'response_rate': 0.8}
    traps = 0
    res = generate_reasoning(candidate, features, traps)
    assert "AI Engineer" in res
    assert "3 AI core skills" in res
