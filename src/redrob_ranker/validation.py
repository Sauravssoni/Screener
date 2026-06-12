import argparse
import csv
import json


def validate_internal(candidates_file, submission_file):
    with open(submission_file, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    assert len(rows) == 100, f"Expected 100 rows, got {len(rows)}"

    seen_ids = set()
    prev_score = float("inf")

    import math

    prev_cid = ""
    for idx, row in enumerate(rows):
        assert "candidate_id" in row
        assert "rank" in row
        assert "score" in row
        assert "reasoning" in row

        cid = row["candidate_id"]
        assert cid not in seen_ids, "duplicate ids"
        seen_ids.add(cid)

        score = float(row["score"])
        assert not math.isnan(score) and not math.isinf(score), "Score is NaN or Inf"

        if score == prev_score:
            assert cid > prev_cid, f"Tie breaker failed: {cid} should be > {prev_cid}"
        assert score <= prev_score, "Score must be non-increasing"

        prev_score = score
        prev_cid = cid

        rank = int(row["rank"])
        assert rank == idx + 1, f"Expected rank {idx + 1}, got {rank}"

        assert row["reasoning"].strip(), "Reasoning is empty"

    reasonings = [r["reasoning"] for r in rows]

    # Verify candidate IDs exist
    valid_ids = set()
    with open(candidates_file, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                c = json.loads(line)
                valid_ids.add(c["candidate_id"])

    for cid in seen_ids:
        assert cid in valid_ids, f"Candidate ID {cid} not found in candidates.jsonl"

    print("Internal validation passed!")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--candidates", required=True)
    parser.add_argument("--submission", required=True)
    args = parser.parse_args()
    validate_internal(args.candidates, args.submission)
