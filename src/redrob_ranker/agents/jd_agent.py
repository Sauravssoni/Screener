def parse_job_description():
    """Parses a job description and returns structured needs.
    Since the challenge prompt specifies fixed criteria (Core AI, Production, Evaluation, Python, Behavioral),
    this agent returns a static structured job representation.
    """
    return {
        "role": "Senior AI Engineer - Founding Team",
        "must_have_skills": ["core_ai", "production", "evaluation_frameworks", "python_systems"],
        "nice_to_have_skills": ["mlops", "leadership"],
        "seniority_band": {"min_yoe": 4, "max_yoe": 12, "ideal_yoe_range": [4, 12]},
        "production_requirements": True,
        "evaluation_requirements": True,
        "behavioral_preferences": {
            "active_on_github": True,
            "open_to_work": True,
            "high_response_rate": True,
            "profile_completeness_min": 0.8,
        },
        "location_constraints": {
            "ideal_locations": ["pune", "noida", "delhi", "gurgaon", "bangalore", "bengaluru"],
            "relocation_acceptable": True,
        },
    }
