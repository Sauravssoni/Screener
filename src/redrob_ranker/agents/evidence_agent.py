from src.redrob_ranker.features import extract_features


def extract_evidence(candidate):
    """
    Extracts structured evidence from the candidate profile using extract_features.
    Must ground every explanation in profile data. No hallucinated skills.
    """
    features = extract_features(candidate)

    # Build some text-based evidence for the UI to display
    skills = [s.get("name", "") for s in candidate.get("skills", [])]
    signals = candidate.get("redrob_signals", {})

    evidence = {
        "features": features,
        "skills_found": skills[:5],  # Just a sample
        "location": candidate.get("profile", {}).get("location", ""),
        "availability_notice_days": signals.get("notice_period_days", -1),
        "yoe": candidate.get("profile", {}).get("years_of_experience", 0),
        "production_evidence_count": features["production_count"],
        "evaluation_evidence_count": features["evaluation_count"],
    }

    return features, evidence
