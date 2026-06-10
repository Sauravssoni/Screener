import argparse
import csv


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--submission", required=True)
    args = parser.parse_args()

    with open(args.submission, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    print(f"Auditing top {min(20, len(rows))} candidates:")
    for row in rows[:20]:
        print(f"Rank {row['rank']}: {row['candidate_id']} | Score: {row['score']}")
        print(f"Reasoning: {row['reasoning']}\n")


if __name__ == "__main__":
    main()
