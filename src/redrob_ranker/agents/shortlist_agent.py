import json
from src.redrob_ranker.io import write_submission


def get_fit_band(score):
    if score >= 0.8:
        return "Exceptional"
    if score >= 0.6:
        return "Strong"
    if score >= 0.4:
        return "Good"
    return "Borderline"


def generate_shortlist_artifacts(top_100, submission_path, top10_json_path, top100_audit_path, grounding_audit_path):
    """
    Generates required artifacts from the sorted top 100 candidates.
    """
    # 1. Output CSV submission
    write_submission(top_100, submission_path)

    # 2. Output Top 10 JSON for Dashboard
    top10_dashboard = []
    for c in top_100[:10]:
        top10_dashboard.append(
            {
                "rank": c["rank"],
                "candidate_id": c["candidate_id"],
                "score": f"{c['final_score']:.4f}",
                "fit_band": get_fit_band(c["final_score"]),
                "reasoning": c["reasoning"],
                "evidence_tags": [
                    f"AI: {c['features']['core_ai_count']}",
                    f"Prod: {c['features']['production_count']}",
                    f"Eval: {c['features']['evaluation_count']}",
                ],
                "risk_flags": c.get("risk_flags", []),
                "review_status": "pending_review",
            }
        )

    with open(top10_json_path, "w", encoding="utf-8") as f:
        json.dump(top10_dashboard, f, indent=2)

    # 3. Top 100 Audit CSV
    import csv

    with open(top100_audit_path, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["rank", "candidate_id", "score", "core_ai", "production", "evaluation", "traps", "reasoning"])
        for c in top_100:
            writer.writerow(
                [
                    c["rank"],
                    c["candidate_id"],
                    f"{c['final_score']:.4f}",
                    c["features"]["core_ai_count"],
                    c["features"]["production_count"],
                    c["features"]["evaluation_count"],
                    c["traps"],
                    c["reasoning"],
                ]
            )

    # 4. Top 20 Grounding Audit MD
    with open(grounding_audit_path, "w", encoding="utf-8") as f:
        f.write("# Top 20 Grounding Audit\n\n")
        for c in top_100[:20]:
            f.write(f"## Rank {c['rank']}: {c['candidate_id']}\n")
            f.write(f"- Score: {c['final_score']:.4f}\n")
            f.write(f"- Reasoning: {c['reasoning']}\n")
            f.write(
                f"- Evidence Grounding: Found {c['evidence']['production_evidence_count']} production keywords, {c['evidence']['evaluation_evidence_count']} eval keywords.\n"
            )
            f.write(f"- Top Skills Matched: {', '.join(c['evidence']['skills_found'])}\n\n")
