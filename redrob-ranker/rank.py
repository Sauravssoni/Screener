import argparse
import time
from src.redrob_ranker.io import stream_candidates, write_submission
from src.redrob_ranker.scoring import score_candidates

def limit_diversity(scored, limit=100):
    from collections import defaultdict
    selected = []
    cluster_counts = defaultdict(int)
    for c in scored:
        title = c.get('profile', {}).get('current_title', 'Unknown')
        score = c['final_score']
        # simple cluster key: title
        cluster_key = title
        
        count = cluster_counts[cluster_key]
        if count >= 3 and len(selected) < 10:
            continue
        if count >= 8 and len(selected) < 50:
            continue
        if count >= 15 and len(selected) < 100:
            continue
            
        selected.append(c)
        cluster_counts[cluster_key] += 1
        if len(selected) == limit:
            break
            
    # if we couldn't find enough, backfill
    if len(selected) < limit:
        for c in scored:
            if c not in selected:
                selected.append(c)
            if len(selected) == limit:
                break
    return selected

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--candidates", required=True, help="Path to candidates.jsonl")
    parser.add_argument("--out", required=True, help="Path for output submission.csv")
    args = parser.parse_args()

    start_time = time.time()
    
    # Process candidates
    scored_candidates = score_candidates(args.candidates)
    
    # Sort and slice top 100
    scored_candidates = sorted(scored_candidates, key=lambda x: (-x['final_score'], x['candidate_id']))
    top_100 = limit_diversity(scored_candidates, 100)
    top_100 = sorted(top_100, key=lambda x: (-x['final_score'], x['candidate_id']))
    
    # Ranks
    for idx, c in enumerate(top_100):
        c['rank'] = idx + 1
        
    write_submission(top_100, args.out)
    
    print(f"Ranking completed in {time.time() - start_time:.2f} seconds")

if __name__ == "__main__":
    main()
