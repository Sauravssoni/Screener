from src.redrob_ranker.features import detect_traps


def evaluate_risks(candidate, features):
    """
    Detects keyword-stuffing traps, impossible expert skill durations, etc.
    Returns number of traps and boolean list of risk flags for UI.
    """
    traps = detect_traps(candidate, features)

    risk_flags = []

    skills = candidate.get("skills", [])
    for s in skills:
        if s.get("proficiency") == "expert" and s.get("duration_months", 0) < 6:
            risk_flags.append(f"Impossible expert skill duration: {s.get('name')}")

    if features["core_ai_count"] > 5 and features["production_count"] == 0:
        risk_flags.append("High AI keywords but no production verbs")

    history = candidate.get("career_history", [])
    sum_months = sum(h.get("duration_months", 0) for h in history)
    declared_months = candidate.get("profile", {}).get("years_of_experience", 0) * 12
    if abs(sum_months - declared_months) > 24:
        risk_flags.append("YOE inconsistency detected")

    signals = candidate.get("redrob_signals", {})
    if signals.get("notice_period_days", 0) > 60 and not signals.get("open_to_work_flag", False):
        risk_flags.append("High notice period and not open to work")

    if features["is_research_only"]:
        risk_flags.append("Profile seems research-only")

    if features["is_manager_only"]:
        risk_flags.append("Profile seems manager-only")

    return traps, risk_flags
