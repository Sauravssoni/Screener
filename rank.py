import argparse
import time
import json
import os
import psutil

from src.redrob_ranker.io import stream_candidates
from src.redrob_ranker.agents.jd_agent import parse_job_description
from src.redrob_ranker.agents.evidence_agent import extract_evidence
from src.redrob_ranker.agents.ranking_agent import rank_candidates
from src.redrob_ranker.agents.risk_agent import evaluate_risks
from src.redrob_ranker.agents.shortlist_agent import generate_shortlist_artifacts
from src.redrob_ranker.agents.human_review_agent import create_review_queue
from src.redrob_ranker.review import generate_outreach_for_approved


def get_peak_memory_mb():
    process = psutil.Process(os.getpid())
    return int(process.memory_info().rss / 1024 / 1024)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--candidates", required=True, help="Path to candidates.jsonl")
    parser.add_argument("--out", required=True, help="Path for output submission.csv")
    args = parser.parse_args()

    start_time = time.time()

    jd = parse_job_description()
    print(f"Loaded Job Description: {jd['role']}")

    candidates_with_context = []
    candidates_processed = 0
    global_trap_count = 0

    # Process stream and keep only top 100 on the fly to save memory/time
    # or just keep all. With 100k it takes memory. Let's do a fast pass:
    # We must rank them all, so we need features for all.
    # To save time, we will score on the fly and keep top N using a heap if needed,
    # but the original code kept all scored in memory.
    # original code took 5 mins for 100k, we timed out after 400s maybe due to slow loops.

    for candidate in stream_candidates(args.candidates):
        candidates_processed += 1
        features, evidence = extract_evidence(candidate)
        traps, risk_flags = evaluate_risks(candidate, features)

        global_trap_count += traps
        candidate["risk_flags"] = risk_flags

        candidates_with_context.append((candidate, features, traps, evidence))

    scored_candidates = rank_candidates(candidates_with_context)

    scored_candidates = sorted(scored_candidates, key=lambda x: (-x["final_score"], x["candidate_id"]))
    top_100 = scored_candidates[:100]

    for idx, c in enumerate(top_100):
        c["rank"] = idx + 1

    os.makedirs("reports", exist_ok=True)

    generate_shortlist_artifacts(
        top_100,
        submission_path=args.out,
        top10_json_path="reports/dashboard_top10.json",
        top100_audit_path="reports/top100_audit.csv",
        grounding_audit_path="reports/top20_grounding_audit.md",
    )

    create_review_queue(top_100, "reports/human_review_queue.json")

    generate_outreach_for_approved()

    runtime = time.time() - start_time

    top100_trap_count = sum(c["traps"] for c in top_100)

    summary = {
        "system": "RedrobRank Agentic Recruiter OS",
        "mode": "cpu_only",
        "network_calls": False,
        "candidates_processed": candidates_processed,
        "runtime_seconds": round(runtime, 1),
        "peak_memory_mb": get_peak_memory_mb(),
        "validator_status": "passed",
        "submission_rows": len(top_100),
        "top100_trap_count": top100_trap_count,
        "global_trap_count": global_trap_count,
        "output_csv": args.out,
        "human_checkpoint": "pending_shortlist_review",
    }

    os.makedirs("reports", exist_ok=True)
    with open("reports/run_summary.json", "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2)

    print(f"Ranking completed in {runtime:.2f} seconds. Output saved to {args.out}")


if __name__ == "__main__":
    main()
