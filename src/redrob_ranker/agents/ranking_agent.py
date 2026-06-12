from src.redrob_ranker.reasoning import generate_reasoning

def rank_candidates(candidates_with_context):
    """
    Ranks candidates using deterministic scoring logic to preserve original functionality.
    candidates_with_context is a list of tuples: (candidate_dict, features, traps, evidence)
    """
    scored = []

    for candidate, features, traps, evidence in candidates_with_context:
        # Replicating original deterministic logic exactly with new weights
        core_ai = min(features["core_ai_count"] / 4.0, 1.0)
        prod = min(features["production_count"] / 3.0, 1.0)
        eval_score = min(features["evaluation_count"] / 2.0, 1.0)
        python = min(features["python_systems_count"] / 4.0, 1.0)

        # 35% AI, 20% production, 15% eval, 10% python, 10% yoe, 5% loc, 5% behavior
        
        yoe_score = features["yoe_ideal"] - (features["yoe_too_junior"] * 0.5)
        yoe_score = max(yoe_score, 0)

        behavioral = (
            features["profile_completeness"] * 0.4 + features["response_rate"] * 0.4 + features["open_to_work"] * 0.2
        )

        location = max(features["ideal_location"], features["willing_to_relocate"] * 0.5)

        final_score = (
            0.35 * core_ai
            + 0.20 * prod
            + 0.15 * eval_score
            + 0.10 * python
            + 0.10 * yoe_score
            + 0.05 * behavioral
            + 0.05 * location
        )

        # Hard Penalties
        if features["is_non_tech"] and features["core_ai_count"] < 2:
            final_score = 0.0
        elif features["is_research_only"] and features["production_count"] == 0:
            final_score = 0.0
        elif features["is_manager_only"] and features["python_systems_count"] == 0:
            final_score = 0.0
        elif features["is_prompt_only"]:
            final_score *= 0.5
        elif features["yoe_too_junior"] and features["core_ai_count"] < 3:
            final_score *= 0.5

        final_score = max(final_score - (traps * 0.15), 0.0)

        candidate["final_score"] = final_score
        candidate["features"] = features
        candidate["traps"] = traps
        candidate["evidence"] = evidence

        candidate["reasoning"] = generate_reasoning(candidate, features, traps, evidence)

        scored.append(candidate)

    # Sort strictly by score descending, then candidate_id ascending for deterministic tie break
    return sorted(scored, key=lambda x: (-x["final_score"], x["candidate_id"]))
