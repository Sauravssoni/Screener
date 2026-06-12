def test_features():
    from src.redrob_ranker.features import normalize_text

    assert normalize_text("Python") == "python"


def test_validation():
    import csv
    import os

    sub_file = "submissions/submission.csv"
    if not os.path.exists(sub_file):
        return  # skip if not generated yet

    assert os.path.getsize(sub_file) <= 5 * 1024 * 1024, "File exceeds 5MB limit"

    with open(sub_file, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    assert len(rows) == 100
    seen_ids = set()
    prev_score = float("inf")

    for idx, row in enumerate(rows):
        assert "candidate_id" in row
        assert "rank" in row
        assert "score" in row
        assert "reasoning" in row

        cid = row["candidate_id"]
        assert cid not in seen_ids
        seen_ids.add(cid)

        score = float(row["score"])
        assert score <= prev_score
        prev_score = score

        rank = int(row["rank"])
        assert rank == idx + 1

        assert row["reasoning"].strip()
