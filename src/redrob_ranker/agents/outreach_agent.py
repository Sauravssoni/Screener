import json
import os


def draft_outreach_for_candidates(approved_candidates, drafts_json_path, packets_dir):
    """
    Generates local draft outreach only for approved candidates.
    Outputs to JSON and generates markdown packets.
    No network calls.
    """
    drafts = []

    if not os.path.exists(packets_dir):
        os.makedirs(packets_dir)

    for c in approved_candidates:
        cid = c["candidate_id"]

        draft_text = (
            f"Subject: Redrob - Founding Senior AI Engineer Role\n\n"
            f"Hi,\n\n"
            f"I came across your profile and noticed your strong background in {', '.join(c['evidence'].get('skills_found', [])[:2])}. "
            f"Given your experience with production AI systems and evaluation frameworks, I think you'd be a great fit for a founding role we're working on.\n\n"
            f"Are you open to a quick chat?\n\nBest,\nRedrob Team"
        )

        drafts.append({"candidate_id": cid, "draft_email": draft_text, "status": "draft_generated"})

        # Recruiter packet
        packet_path = os.path.join(packets_dir, f"{cid}.md")
        with open(packet_path, "w", encoding="utf-8") as f:
            f.write(f"# Recruiter Packet: {cid}\n\n")
            f.write(f"## Why Shortlisted\nRanked {c.get('rank', 'N/A')} with score {c.get('score', 0):.4f}.\n")
            f.write("Strong match for production retrieval systems and evaluation.\n\n")
            f.write("## Risk Flags\n")
            if c.get("risk_flags"):
                for flag in c["risk_flags"]:
                    f.write(f"- {flag}\n")
            else:
                f.write("- None detected.\n")
            f.write("\n## Suggested Interview Questions\n")
            f.write("- Can you describe the tradeoffs between dense vector search and BM25 in a production setting?\n")
            f.write("- How do you evaluate ranking relevance offline vs online (e.g., NDCG vs A/B testing)?\n")
            f.write("- What strategies do you use for latency reduction during large-scale inference?\n\n")
            f.write(f"## Draft Outreach\n```text\n{draft_text}\n```\n")

    with open(drafts_json_path, "w", encoding="utf-8") as f:
        json.dump(drafts, f, indent=2)

    return drafts
