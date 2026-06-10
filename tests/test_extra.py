def test_text_tokens():
    from src.redrob_ranker.text import extract_tokens, count_terms, has_exact_match

    assert count_terms("hello world", ["world"]) == 1
    assert has_exact_match("hello world", "world")
    assert "hello" in extract_tokens("hello world")


def test_extract_features():
    from src.redrob_ranker.features import extract_features, detect_traps

    c = {
        "profile": {"current_title": "AI Engineer", "years_of_experience": 5},
        "skills": [{"name": "python", "proficiency": "expert", "duration_months": 2}],
        "redrob_signals": {"response_rate": 0.8},
    }
    f = extract_features(c)
    assert f["core_ai_count"] == 0

    t = detect_traps(c, f)
    assert t > 0  # trap for tiny expert duration
