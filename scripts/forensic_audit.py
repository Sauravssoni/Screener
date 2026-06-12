import csv
import json
import argparse
import sys
import os


def load_candidates(path):
    candidates = {}
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                try:
                    c = json.loads(line)
                    candidates[c["candidate_id"]] = c
                except json.JSONDecodeError:
                    pass
    return candidates


def load_submission(path):
    rows = []
    with open(path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for r in reader:
            rows.append(r)
    return rows


def check_hallucinations():
    parser = argparse.ArgumentParser()
    parser.add_argument("--csv", required=True)
    parser.add_argument("--jsonl", required=True)
    parser.add_argument("--out", required=True)
    args = parser.parse_args()

    candidates = load_candidates(args.jsonl)
    submission = load_submission(args.csv)

    failures = 0
    unique_scores = set()
    unique_reasoning = set()

    report_lines = []
    report_lines.append("# Forensic Audit Report\n")

    top_20 = []

    prev_score = float("inf")

    for idx, row in enumerate(submission):
        cid = row["candidate_id"]
        if cid not in candidates:
            print(f"FAIL: Candidate {cid} not found in jsonl")
            failures += 1
            continue

        c = candidates[cid]
        reason = row["reasoning"]
        score = float(row["score"])
        rank = int(row["rank"])

        unique_scores.add(score)
        unique_reasoning.add(reason)

        if rank != idx + 1:
            print(f"FAIL: Rank mismatch at {idx}, expected {idx + 1}, got {rank}")
            failures += 1
        if score > prev_score:
            print(f"FAIL: Score is not non-increasing at {idx}, score {score} > {prev_score}")
            failures += 1
        prev_score = score

        title = c["profile"].get("current_title", "").lower()
        yoe = float(c["profile"].get("years_of_experience", 0.0))
        yoe_str = f"{yoe:.1f}"
        location = c["profile"].get("location", "").lower()
        country = c["profile"].get("country", "").lower()

        concerns = []

        if title and title not in reason.lower():
            # Weak check to allow variants but flag explicit mismatch
            # Example: "Senior Machine Learning Engineer" might just say "Machine Learning Engineer"
            if not any(word in reason.lower() for word in title.split()):
                concerns.append("Title mismatch")

        if yoe_str not in reason:
            concerns.append("YOE mismatch")

        loc_match = False
        if location and location in reason.lower():
            loc_match = True
        if country and country in reason.lower():
            loc_match = True
        if not loc_match and (location or country):
            concerns.append("Location mismatch")

        # Non-fit check
        if idx < 50:
            if any(term in title for term in ["manager", "director", "vp", "head"]) and not any(
                term in title for term in ["engineering", "data", "ai", "machine learning"]
            ):
                concerns.append("Manager non-fit in top 50")
            if any(term in title for term in ["support", "hr", "sales", "marketing", "accountant", "civil"]):
                concerns.append("Obvious non-fit in top 50")

        if concerns:
            failures += 1

        if idx < 20:
            top_20.append(
                {
                    "rank": rank,
                    "cid": cid,
                    "actual_title": c["profile"].get("current_title", ""),
                    "yoe": yoe_str,
                    "location": c["profile"].get("location", ""),
                    "score": score,
                    "concerns": ", ".join(concerns) if concerns else "None",
                }
            )

    if len(unique_scores) < 20:
        print(f"FAIL: unique_scores ({len(unique_scores)}) < 20")
        failures += 1
    if len(unique_reasoning) < 90:
        print(f"FAIL: unique_reasoning ({len(unique_reasoning)}) < 90")
        failures += 1

    report_lines.append(f"- **Unique Scores**: {len(unique_scores)}")
    report_lines.append(f"- **Unique Reasonings**: {len(unique_reasoning)}")
    report_lines.append(f"- **Hallucination / Rule Failures**: {failures}\n")
    report_lines.append("## Top 20 Candidates\n")
    report_lines.append("| Rank | Candidate ID | Actual Title | YOE | Location | Score | Concerns |")
    report_lines.append("|---|---|---|---|---|---|---|")

    for r in top_20:
        report_lines.append(
            f"| {r['rank']} | {r['cid']} | {r['actual_title']} | {r['yoe']} | {r['location']} | {r['score']} | {r['concerns']} |"
        )

    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    with open(args.out, "w") as f:
        f.write("\n".join(report_lines))

    if failures > 0:
        print(f"Forensic audit failed with {failures} errors.")
        sys.exit(1)
    else:
        print("Forensic audit passed successfully.")


if __name__ == "__main__":
    check_hallucinations()
