import argparse
import csv


def main():
    parser = argparse.ArgumentParser()
    # Support both named arguments and positional fallback
    parser.add_argument("--candidates", required=False)
    parser.add_argument("--submission", required=False)
    parser.add_argument("submission_positional", nargs="?", default=None)

    args = parser.parse_args()

    sub_file = args.submission or args.submission_positional
    if not sub_file:
        parser.error("the following arguments are required: submission")

    with open(sub_file, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    assert len(rows) == 100, f"Expected 100 rows, got {len(rows)}"

    seen_ids = set()
    prev_score = float("inf")

    for idx, row in enumerate(rows):
        assert "candidate_id" in row
        assert "rank" in row
        assert "score" in row
        assert "reasoning" in row

        cid = row["candidate_id"]
        assert cid not in seen_ids, "duplicate ids"
        seen_ids.add(cid)

        score = float(row["score"])
        assert score <= prev_score, "Score must be non-increasing"
        prev_score = score

        rank = int(row["rank"])
        assert rank == idx + 1, f"Expected rank {idx + 1}, got {rank}"

        assert row["reasoning"].strip(), "Reasoning is empty"

    print("Success: Submission validated!")


if __name__ == "__main__":
    main()
