import argparse
import time
from src.redrob_ranker.io import stream_candidates, write_submission
from src.redrob_ranker.scoring import score_candidates

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--candidates", required=True, help="Path to candidates.jsonl")
    parser.add_argument("--out", required=True, help="Path for output submission.csv")
    args = parser.parse_args()

    start_time = time.time()
    
    # Process candidates
    scored_candidates = score_candidates(args.candidates)
    
    # Sort and slice top 100
    top_100 = sorted(scored_candidates, key=lambda x: x['final_score'], reverse=True)[:100]
    
    # Ranks
    for idx, c in enumerate(top_100):
        c['rank'] = idx + 1
        
    write_submission(top_100, args.out)
    
    print(f"Ranking completed in {time.time() - start_time:.2f} seconds")

if __name__ == "__main__":
    main()
