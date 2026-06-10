import json

input_data = [
  {
    "candidate_id": "CAND_0000001",
    "profile": {
      "anonymized_name": "Ira Vora",
      "headline": "Backend Engineer | SQL, Spark, Cloud",
      "summary": "Software / data professional with 6.9 years of experience building data pipelines, backend systems, and analytics infrastructure. I'm a backend/data hybrid — Spark, Airflow, SQL warehouses are home territory; I'm building competence on the ML side. My toolkit is solid on the data engineering side — Python, SQL, Spark, Airflow, warehouse design — and I've completed a couple of self-directed ML projects (Kaggle competitions, side projects fine-tuning small models). Interested in transitioning toward more AI/ML-focused work, ideally at a company where I can leverage my existing data-infra skills while learning modern ML practice.",
      "location": "Toronto",
      "country": "Canada",
      "years_of_experience": 6.9,
      "current_title": "Backend Engineer",
      "current_company": "Mindtree",
      "current_company_size": "10001+",
      "current_industry": "IT Services"
    },
    "career_history": [
      {
        "company": "Mindtree",
        "title": "Backend Engineer",
        "start_date": "2024-03-08",
        "end_date": None,
        "duration_months": 27,
        "is_current": True,
        "industry": "IT Services",
        "company_size": "10001+",
        "description": "Implemented streaming data pipelines on Kafka and Spark Streaming for a real-time user-activity processing platform. Designed the schema-registry integration, the watermark/state management approach, and the deduplication logic for late-arriving events. Worked closely with the data science team to make sure feature pipelines aligned with what their models needed. Most of my career has been data engineering, with some adjacent ML exposure."
      },
       {
        "company": "Swiggy",
        "title": "Recommendation Systems Engineer",
        "start_date": "2025-04-02",
        "end_date": None,
        "duration_months": 14,
        "is_current": True,
        "industry": "Food Delivery",
        "company_size": "5001-10000",
        "description": "Trained and shipped multiple ranking models for our product's discovery feed using XGBoost and LightGBM. Designed features across three families: content metadata, user behavior signals, and item engagement history. Owned the offline-online correlation analysis that determined which offline metrics actually predicted A/B test outcomes. Worked closely with PMs to define the optimization target (click-through vs. dwell time vs. downstream conversion) — that work was as important as the modeling itself."
      },
      {
        "company": "Mad Street Den",
        "title": "Search Engineer",
        "start_date": "2023-10-10",
        "end_date": "2025-02-01",
        "duration_months": 16,
        "is_current": False,
        "industry": "AI/ML",
        "company_size": "201-500",
        "description": "Trained and shipped multiple ranking models for our product's discovery feed using XGBoost and LightGBM. Designed features across three families: content metadata, user behavior signals, and item engagement history. Owned the offline-online correlation analysis that determined which offline metrics actually predicted A/B test outcomes. Worked closely with PMs to define the optimization target (click-through vs. dwell time vs. downstream conversion) — that work was as important as the modeling itself."
      }
    ],
    "skills": [
      {
        "name": "Tailwind",
        "proficiency": "intermediate",
        "endorsements": 3,
        "duration_months": 13
      },
      {
        "name": "NLP",
        "proficiency": "advanced",
        "endorsements": 37,
        "duration_months": 26
      }
    ],
    "redrob_signals": {
      "profile_completeness_score": 86.9,
      "signup_date": "2025-10-16",
      "last_active_date": "2026-05-20",
      "open_to_work_flag": True,
      "profile_views_received_30d": 23,
      "applications_submitted_30d": 2,
      "recruiter_response_rate": 0.34,
      "avg_response_time_hours": 177.8,
      "skill_assessment_scores": {
        "NLP": 38.8,
        "Image Classification": 64.8,
        "Fine-tuning LLMs": 41.6,
        "Speech Recognition": 53.7
      },
      "connection_count": 356,
      "endorsements_received": 35,
      "notice_period_days": 60,
      "expected_salary_range_inr_lpa": {
        "min": 18.7,
        "max": 36.1
      },
      "preferred_work_mode": "onsite",
      "willing_to_relocate": False,
      "github_activity_score": 9.2,
      "search_appearance_30d": 249,
      "saved_by_recruiters_30d": 4,
      "interview_completion_rate": 0.71,
      "offer_acceptance_rate": 0.58,
      "verified_email": True,
      "verified_phone": True,
      "linkedin_connected": False
    }
  },
  {
    "candidate_id": "CAND_0000031",
    "profile": {
      "anonymized_name": "Ela Singh",
      "headline": "Recommendation Systems Engineer | Search, Ranking & Retrieval",
      "summary": "Machine learning engineer with 6.0 years of experience building ML-powered features in production. Strong background in NLP, recommendation systems, and applied AI; comfortable across the ML stack from feature engineering through deployment. Recently, I led the team that migrated our keyword-search-based product to embedding-based retrieval. I've learned that most retrieval problems are actually evaluation problems in disguise. My academic background is in CS/ML but my main learning has come from shipping real systems and seeing what holds up under production load. Open to senior IC roles in applied ML or AI engineering, ideally at product companies where I'd own a meaningful piece of the ML stack.",
      "location": "Hyderabad, Telangana",
      "country": "India",
      "years_of_experience": 6.0,
      "current_title": "Recommendation Systems Engineer",
      "current_company": "Swiggy",
      "current_company_size": "5001-10000",
      "current_industry": "Food Delivery"
    },
    "career_history": [
      {
        "company": "Swiggy",
        "title": "Recommendation Systems Engineer",
        "start_date": "2025-04-02",
        "end_date": None,
        "duration_months": 14,
        "is_current": True,
        "industry": "Food Delivery",
        "company_size": "5001-10000",
        "description": "Trained and shipped multiple ranking models for our product's discovery feed using XGBoost and LightGBM. Designed features across three families: content metadata, user behavior signals, and item engagement history. Owned the offline-online correlation analysis that determined which offline metrics actually predicted A/B test outcomes. Worked closely with PMs to define the optimization target (click-through vs. dwell time vs. downstream conversion) — that work was as important as the modeling itself."
      },
      {
        "company": "Mad Street Den",
        "title": "Search Engineer",
        "start_date": "2023-10-10",
        "end_date": "2025-02-01",
        "duration_months": 16,
        "is_current": False,
        "industry": "AI/ML",
        "company_size": "201-500",
        "description": "Trained and shipped multiple ranking models for our product's discovery feed using XGBoost and LightGBM. Designed features across three families: content metadata, user behavior signals, and item engagement history. Owned the offline-online correlation analysis that determined which offline metrics actually predicted A/B test outcomes. Worked closely with PMs to define the optimization target (click-through vs. dwell time vs. downstream conversion) — that work was as important as the modeling itself."
      },
      {
        "company": "Uber",
        "title": "NLP Engineer",
        "start_date": "2021-07-22",
        "end_date": "2023-10-10",
        "duration_months": 27,
        "is_current": False,
        "industry": "Transportation",
        "company_size": "10001+",
        "description": "Trained and shipped multiple ranking models for our product's discovery feed using XGBoost and LightGBM. Designed features across three families: content metadata, user behavior signals, and item engagement history. Owned the offline-online correlation analysis that determined which offline metrics actually predicted A/B test outcomes. Worked closely with PMs to define the optimization target (click-through vs. dwell time vs. downstream conversion) — that work was as important as the modeling itself."
      },
      {
        "company": "Zomato",
        "title": "Applied ML Engineer",
        "start_date": "2020-06-27",
        "end_date": "2021-07-22",
        "duration_months": 13,
        "is_current": False,
        "industry": "Food Delivery",
        "company_size": "5001-10000",
        "description": "Owned the ranking layer for an e-commerce search product, evolving it from a hand-tuned scoring function to a learning-to-rank model over 9 months. Designed the relevance labeling pipeline (mix of click-through data and explicit human judgments), the feature pipeline, and the training/eval workflow. Most of the work was infrastructure and data quality — the modeling part was almost the easy bit. Final model improved revenue-per-search by 12%."
      }
    ],
    "education": [
      {
        "institution": "SRM University",
        "degree": "M.Tech",
        "field_of_study": "Computer Engineering",
        "start_year": 2002,
        "end_year": 2006,
        "grade": "9.16 CGPA",
        "tier": "tier_2"
      }
    ],
    "skills": [
      {
        "name": "Go",
        "proficiency": "intermediate",
        "endorsements": 7,
        "duration_months": 19
      },
      {
        "name": "MLflow",
        "proficiency": "advanced",
        "endorsements": 59,
        "duration_months": 21
      },
      {
        "name": "FAISS",
        "proficiency": "advanced",
        "endorsements": 19,
        "duration_months": 35
      },
      {
        "name": "Pinecone",
        "proficiency": "expert",
        "endorsements": 34,
        "duration_months": 88
      },
      {
        "name": "Sentence Transformers",
        "proficiency": "expert",
        "endorsements": 16,
        "duration_months": 69
      }
    ],
    "redrob_signals": {
      "profile_completeness_score": 83.4,
      "signup_date": "2026-01-28",
      "last_active_date": "2026-05-24",
      "open_to_work_flag": True,
      "profile_views_received_30d": 194,
      "applications_submitted_30d": 2,
      "recruiter_response_rate": 0.91,
      "avg_response_time_hours": 76.1,
      "connection_count": 832,
      "endorsements_received": 177,
      "notice_period_days": 60,
      "preferred_work_mode": "flexible",
      "willing_to_relocate": True,
      "github_activity_score": 32.6,
      "verified_email": False,
      "verified_phone": True,
      "linkedin_connected": False
    }
  }
]

import random
# Generate 100 fake candidates
with open('candidates.jsonl', 'w') as f:
    for i in range(100000):
        c = dict(input_data[i % len(input_data)])
        c['candidate_id'] = f"CAND_{str(i+2).zfill(7)}"
        f.write(json.dumps(c) + '\n')
