def validate_top_candidates(candidates):
    assert len(candidates) == 100, f"Expected 100 candidates, got {len(candidates)}"
    
    seen_ids = set()
    prev_score = float('inf')
    
    for c in candidates:
        cid = c['candidate_id']
        assert cid not in seen_ids, f"Duplicate candidate_id: {cid}"
        seen_ids.add(cid)
        
        score = c['final_score']
        assert score <= prev_score, f"Scores not non-increasing: {score} > {prev_score}"
        prev_score = score
        
        assert c.get('reasoning'), "Reasoning cannot be empty"
        assert c.get('rank') is not None, "Rank missing"
