import json
import os
from src.redrob_ranker.agents.outreach_agent import draft_outreach_for_candidates


def load_review_queue(filepath="reports/human_review_queue.json"):
    if not os.path.exists(filepath):
        return []
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)


def save_review_queue(queue, filepath="reports/human_review_queue.json"):
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(queue, f, indent=2)


def set_candidate_status(candidate_id, status, filepath="reports/human_review_queue.json"):
    assert status in ["pending_review", "approved", "hold", "rejected"]
    queue = load_review_queue(filepath)
    for c in queue:
        if c["candidate_id"] == candidate_id:
            c["status"] = status
            break
    save_review_queue(queue, filepath)


def get_approved_candidates(filepath="reports/human_review_queue.json"):
    queue = load_review_queue(filepath)
    return [c for c in queue if c["status"] == "approved"]


def generate_outreach_for_approved(
    queue_path="reports/human_review_queue.json",
    drafts_path="reports/outreach_drafts.json",
    packets_dir="reports/recruiter_packets",
):
    approved = get_approved_candidates(queue_path)
    # If none approved, generate empty list with explanation is handled inherently by empty list
    draft_outreach_for_candidates(approved, drafts_path, packets_dir)
