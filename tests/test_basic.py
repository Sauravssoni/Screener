def test_features():
    from src.redrob_ranker.features import count_terms
    assert count_terms("I built an a/b test pipeline", ["a/b test"]) == 1
    assert count_terms("No skills here", ["a/b test"]) == 0

def test_validation():
    from src.redrob_ranker.validation import validate_top_candidates
    candidates = [{"candidate_id": str(i), "final_score": 100 - i, "reasoning": "Reason", "rank": i+1} for i in range(100)]
    validate_top_candidates(candidates)
