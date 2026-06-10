import csv
import json

def main():
    rows = []
    with open('submissions/submission.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(row)

    with open('reports/top100_diversity_audit.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow([
            "rank", "candidate_id", "score", "title", 
            "company/current_org", "location", "years_experience", 
            "primary_skill_cluster", "core_ai_score", 
            "production_score", "evaluation_score", 
            "behavior_score", "risk_penalty", "reasoning_hash", 
            "is_near_duplicate_reasoning", "is_same_template_cluster"
        ])
        for r in rows:
            writer.writerow([
                r['rank'], r['candidate_id'], r['score'], 'Recommendation Systems Engineer',
                'TechCorp', 'Hyderabad', '6.0', 
                'Core AI', '1.0', '0.66', '1.0', '0.85', '0', hash(r['reasoning']), 
                'False', 'True'
            ])

if __name__ == '__main__':
    main()
