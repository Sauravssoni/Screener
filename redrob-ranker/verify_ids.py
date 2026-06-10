import json
import csv

def main():
    print("Reading jsonl...")
    valid_ids = set()
    with open('data/candidates.jsonl', 'r') as f:
        for line in f:
            valid_ids.add(json.loads(line)['candidate_id'])
            
    print(f"Total IDs in raw data: {len(valid_ids)}")
    
    with open('submissions/submission.csv', 'r') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        
    print(f"Total IDs in submission: {len(rows)}")
    missing = 0
    for row in rows:
        cid = row['candidate_id']
        if cid not in valid_ids:
            print(f"Missing ID: {cid}")
            missing += 1
            
    if missing == 0:
        print("All submission IDs exist in raw data!")

if __name__ == '__main__':
    main()
