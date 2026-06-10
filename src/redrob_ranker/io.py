import json
import csv


def stream_candidates(filepath):
    """Yields candidate dicts from a JSONL file."""
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                yield json.loads(line)


def write_submission(candidates, filepath):
    """Writes the final 100 candidates to CSV."""
    with open(filepath, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["candidate_id", "rank", "score", "reasoning"])
        for c in candidates:
            writer.writerow([c["candidate_id"], c["rank"], f"{c['final_score']:.4f}", c["reasoning"]])
