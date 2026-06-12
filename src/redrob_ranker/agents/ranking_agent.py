from src.redrob_ranker.reasoning import generate_reasoning
from collections import defaultdict


def limit_diversity(scored):
    """
    Limits the number of candidates with near-identical template profiles.
    max 3 same cluster in top 10, max 8 in top 50, max 15 in top 100.
    Since we must maintain non-increasing score order, we apply a tiny
    penalty to final_score for candidates that exceed the cluster limits.
    """
    cluster_counts = defaultdict(int)

    # Sort first by raw score to process in order of merit
    scored = sorted(scored, key=lambda x: (-x["final_score"], x["candidate_id"]))

    adjusted = []
    for rank, c in enumerate(scored):
        title = c.get("profile", {}).get("current_title", "Unknown")
        primary_skill = c.get("features", {}).get("primary_skill_cluster", "Unknown")
        cluster_key = f"{title}_{primary_skill}"

        count = cluster_counts[cluster_key]
        penalty = 0.0

        # Check thresholds based on current position
        if rank < 10 and count >= 3:
            penalty = 0.0001 + (count * 0.00001)
        elif rank < 50 and count >= 8:
            penalty = 0.0001 + (count * 0.00001)
        elif rank < 100 and count >= 15:
            penalty = 0.0001 + (count * 0.00001)

        c["final_score"] = max(0.0, c["final_score"] - penalty)
        cluster_counts[cluster_key] += 1
        adjusted.append(c)

    # Re-sort using the adjusted score
    adjusted = sorted(adjusted, key=lambda x: (-x["final_score"], x["candidate_id"]))
    return adjusted


def rank_candidates(candidates_with_context):
    """
    Ranks candidates using deterministic scoring logic to preserve original functionality.
    candidates_with_context is a list of tuples: (candidate_dict, features, traps, evidence)
    """
    scored = []

    for candidate, features, traps, evidence in candidates_with_context:
        # Replicating original deterministic logic exactly
        core_ai = min(features["core_ai_count"] / 5.0, 1.0)
        prod = min(features["production_count"] / 3.0, 1.0)
        eval_score = min(features["evaluation_count"] / 2.0, 1.0)
        python = min(features["python_systems_count"] / 4.0, 1.0)

        career_shape = (
            features["yoe_ideal"]
            - (features["yoe_too_junior"] * 0.5)
            - (features["is_manager_only"] * 0.8)
            - (features["is_research_only"] * 0.3)
        )
        career_shape = max(career_shape, 0)

        behavioral = (
            features["profile_completeness"] * 0.4 + features["response_rate"] * 0.4 + features["open_to_work"] * 0.2
        )

        location = max(features["ideal_location"], features["willing_to_relocate"] * 0.5)

        final_score = (
            0.35 * core_ai
            + 0.18 * prod
            + 0.14 * eval_score
            + 0.10 * python
            + 0.08 * career_shape
            + 0.07 * behavioral
            + 0.04 * location
        ) - (traps * 0.15)

        final_score = max(final_score, 0)

        candidate["final_score"] = final_score
        candidate["features"] = features
        candidate["traps"] = traps
        candidate["evidence"] = evidence

        candidate["reasoning"] = generate_reasoning(candidate, features, traps, evidence)

        scored.append(candidate)

    return limit_diversity(scored)
