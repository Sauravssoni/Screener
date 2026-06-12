def generate_reasoning(candidate, features, traps, evidence=None):
    prof = candidate.get("profile", {})
    title = prof.get("current_title", "Engineer")

    parts = []

    # Technical reasoning
    yoe = evidence.get("yoe", prof.get("years_of_experience", 0)) if evidence else prof.get("years_of_experience", 0)
    loc = evidence.get("location", "") if evidence else ""
    loc_str = f" in {loc}" if loc else ""
    py_count = features.get("python_systems_count", 0)
    comp = features.get("profile_completeness", 0)

    if features["core_ai_count"] > 0:
        skills_str = ""
        if evidence and "skills_found" in evidence and evidence["skills_found"]:
            skills_str = f" (e.g. {', '.join(evidence['skills_found'])})"
        parts.append(
            f"Strong AI search fit: profile evidence includes {features['core_ai_count']} core AI terms{skills_str}{loc_str} with {yoe} YOE, {py_count} python systems, and {comp:.2f} completeness for {title}."
        )

    if features["production_count"] > 0:
        parts.append(
            f"Shows production indicators ({features['production_count']} terms) around deployed retrieval and monitoring."
        )

    if features["evaluation_count"] > 0:
        parts.append("Has evaluation expertise (e.g. NDCG, MAP, offline benchmark).")

    if features["response_rate"] > 0:
        parts.append(f"Redrob signals show a {features['response_rate']:.0%} response rate.")

    if not parts:
        company = prof.get("current_company", "a company")
        parts.append(f"Candidate {title} at {company} fits baseline criteria with {comp:.2f} completeness.")

    if traps > 0:
        parts.append(f"Note: Flagged {traps} risk(s).")

    return " ".join(parts)
