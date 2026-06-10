import pytest

def test_validation():
    from src.redrob_ranker.validation import validate_top_candidates
    candidates = [{"candidate_id": str(i), "final_score": 100 - i, "reasoning": "Reason", "rank": i+1} for i in range(100)]
    validate_top_candidates(candidates)

def test_validation_fails_count():
    from src.redrob_ranker.validation import validate_top_candidates
    candidates = [{"candidate_id": str(i), "final_score": 1, "reasoning": "R", "rank": i+1} for i in range(50)]
    with pytest.raises(AssertionError):
        validate_top_candidates(candidates)
