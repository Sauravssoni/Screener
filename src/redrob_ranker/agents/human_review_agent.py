import json


def create_review_queue(top_100, filepath):
    """
    Creates a local JSON queue for human review checkpoint.
    All candidates default to pending_review.
    """
    queue = []

    # If the file already exists, we might want to preserve status,
    # but for a fresh run we can just overwrite or merge.
    # We will just overwrite for this pipeline to represent a fresh run.

    for c in top_100:
        queue.append(
            {
                "candidate_id": c["candidate_id"],
                "rank": c["rank"],
                "score": c["final_score"],
                "status": "pending_review",
                "risk_flags": c.get("risk_flags", []),
                "evidence": c.get("evidence", {}),
            }
        )

    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(queue, f, indent=2)
