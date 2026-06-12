def test_generate_reasoning():
    from src.redrob_ranker.reasoning import generate_reasoning

    candidate = {
        "candidate_id": "TEST_123",
        "profile": {"current_title": "AI Engineer", "years_of_experience": 5},
        "redrob_signals": {},
    }
    features = {"core_ai_count": 3, "production_count": 1, "evaluation_count": 0, "response_rate": 0.8}
    traps = 0
    res = generate_reasoning(candidate, features, traps)

    assert "production indicators" in res
    assert "evaluation" not in res
    assert res.strip() != ""
    assert "TEST_123" not in res  # Candidate ID not used as filler

    features_no_prod = {"core_ai_count": 3, "production_count": 0, "evaluation_count": 0, "response_rate": 0.8}
    res_no_prod = generate_reasoning(candidate, features_no_prod, traps)
    assert "production" not in res_no_prod.lower()

    features_eval = {"core_ai_count": 3, "production_count": 0, "evaluation_count": 2, "response_rate": 0.0}
    res_eval = generate_reasoning(candidate, features_eval, traps)
    assert "evaluation expertise" in res_eval
