def test_io_stream(tmp_path):
    from src.redrob_ranker.io import stream_candidates
    file = tmp_path / "candidates.jsonl"
    file.write_text('{"candidate_id": "CAND_1"}\n{"candidate_id": "CAND_2"}\n')
    data = list(stream_candidates(str(file)))
    assert len(data) == 2
    assert data[0]['candidate_id'] == "CAND_1"
