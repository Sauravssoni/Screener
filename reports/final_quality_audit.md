# Final Quality & Security Audit
## Pytest
F.FFF.                                                                   [100%]
=================================== FAILURES ===================================
________________________________ test_features _________________________________

    def test_features():
>       from src.redrob_ranker.features import normalize_text
E       ModuleNotFoundError: No module named 'src'

tests/test_basic.py:2: ModuleNotFoundError
_______________________________ test_text_tokens _______________________________

    def test_text_tokens():
>       from src.redrob_ranker.text import extract_tokens, count_terms, has_exact_match
E       ModuleNotFoundError: No module named 'src'

tests/test_extra.py:2: ModuleNotFoundError
____________________________ test_extract_features _____________________________

    def test_extract_features():
>       from src.redrob_ranker.features import extract_features, detect_traps
E       ModuleNotFoundError: No module named 'src'

tests/test_extra.py:10: ModuleNotFoundError
___________________________ test_generate_reasoning ____________________________

    def test_generate_reasoning():
>       from src.redrob_ranker.reasoning import generate_reasoning
E       ModuleNotFoundError: No module named 'src'

tests/test_reasoning.py:2: ModuleNotFoundError
=========================== short test summary info ============================
FAILED tests/test_basic.py::test_features - ModuleNotFoundError: No module na...
FAILED tests/test_extra.py::test_text_tokens - ModuleNotFoundError: No module...
FAILED tests/test_extra.py::test_extract_features - ModuleNotFoundError: No m...
FAILED tests/test_reasoning.py::test_generate_reasoning - ModuleNotFoundError...
4 failed, 2 passed in 0.04s
## Ruff
F401 [*] `io.StringIO` imported but unused
 --> sandbox_app.py:5:16
  |
3 | import pandas as pd
4 | import os
5 | from io import StringIO
  |                ^^^^^^^^
6 |
7 | from src.redrob_ranker.agents.ranking_agent import rank_candidates
  |
help: Remove unused import: `io.StringIO`

F401 [*] `src.redrob_ranker.text.count_terms` imported but unused
 --> src/redrob_ranker/features.py:1:36
  |
1 | from src.redrob_ranker.text import count_terms, normalize_text
  |                                    ^^^^^^^^^^^
2 | import re
  |
help: Remove unused import: `src.redrob_ranker.text.count_terms`

F841 Local variable `struct_score` is assigned to but never used
  --> src/redrob_ranker/reasoning.py:9:5
   |
 7 |     # Retrieve semantic and structural scores
 8 |     sem_score = candidate.get("semantic_score", 0.0)
 9 |     struct_score = candidate.get("struct_score", 0.0)
   |     ^^^^^^^^^^^^
10 |     
11 |     parts = []
   |
help: Remove assignment to unused variable `struct_score`

Found 3 errors.
[*] 2 fixable with the `--fix` option (1 hidden fix can be enabled with the `--unsafe-fixes` option).
## Bandit
[main]	INFO	profile include tests: None
[main]	INFO	profile exclude tests: None
[main]	INFO	cli include tests: None
[main]	INFO	cli exclude tests: None
[main]	INFO	running on Python 3.10.13
Run started:2026-06-12 10:59:10.541618+00:00

Test results:
>> Issue: [B101:assert_used] Use of assert detected. The enclosed code will be removed when compiling to optimised byte code.
   Severity: Low   Confidence: High
   CWE: CWE-703 (https://cwe.mitre.org/data/definitions/703.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b101_assert_used.html
   Location: src/redrob_ranker/review.py:19:4
18	def set_candidate_status(candidate_id, status, filepath="reports/human_review_queue.json"):
19	    assert status in ["pending_review", "approved", "hold", "rejected"]
20	    queue = load_review_queue(filepath)

--------------------------------------------------
>> Issue: [B101:assert_used] Use of assert detected. The enclosed code will be removed when compiling to optimised byte code.
   Severity: Low   Confidence: High
   CWE: CWE-703 (https://cwe.mitre.org/data/definitions/703.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b101_assert_used.html
   Location: src/redrob_ranker/validation.py:11:4
10	
11	    assert len(rows) == 100, f"Expected 100 rows, got {len(rows)}"
12	

--------------------------------------------------
>> Issue: [B101:assert_used] Use of assert detected. The enclosed code will be removed when compiling to optimised byte code.
   Severity: Low   Confidence: High
   CWE: CWE-703 (https://cwe.mitre.org/data/definitions/703.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b101_assert_used.html
   Location: src/redrob_ranker/validation.py:20:8
19	    for idx, row in enumerate(rows):
20	        assert "candidate_id" in row
21	        assert "rank" in row

--------------------------------------------------
>> Issue: [B101:assert_used] Use of assert detected. The enclosed code will be removed when compiling to optimised byte code.
   Severity: Low   Confidence: High
   CWE: CWE-703 (https://cwe.mitre.org/data/definitions/703.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b101_assert_used.html
   Location: src/redrob_ranker/validation.py:21:8
20	        assert "candidate_id" in row
21	        assert "rank" in row
22	        assert "score" in row

--------------------------------------------------
>> Issue: [B101:assert_used] Use of assert detected. The enclosed code will be removed when compiling to optimised byte code.
   Severity: Low   Confidence: High
   CWE: CWE-703 (https://cwe.mitre.org/data/definitions/703.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b101_assert_used.html
   Location: src/redrob_ranker/validation.py:22:8
21	        assert "rank" in row
22	        assert "score" in row
23	        assert "reasoning" in row

--------------------------------------------------
>> Issue: [B101:assert_used] Use of assert detected. The enclosed code will be removed when compiling to optimised byte code.
   Severity: Low   Confidence: High
   CWE: CWE-703 (https://cwe.mitre.org/data/definitions/703.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b101_assert_used.html
   Location: src/redrob_ranker/validation.py:23:8
22	        assert "score" in row
23	        assert "reasoning" in row
24	

--------------------------------------------------
>> Issue: [B101:assert_used] Use of assert detected. The enclosed code will be removed when compiling to optimised byte code.
   Severity: Low   Confidence: High
   CWE: CWE-703 (https://cwe.mitre.org/data/definitions/703.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b101_assert_used.html
   Location: src/redrob_ranker/validation.py:26:8
25	        cid = row["candidate_id"]
26	        assert cid not in seen_ids, "duplicate ids"
27	        seen_ids.add(cid)

--------------------------------------------------
>> Issue: [B101:assert_used] Use of assert detected. The enclosed code will be removed when compiling to optimised byte code.
   Severity: Low   Confidence: High
   CWE: CWE-703 (https://cwe.mitre.org/data/definitions/703.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b101_assert_used.html
   Location: src/redrob_ranker/validation.py:30:8
29	        score = float(row["score"])
30	        assert not math.isnan(score) and not math.isinf(score), "Score is NaN or Inf"
31	

--------------------------------------------------
>> Issue: [B101:assert_used] Use of assert detected. The enclosed code will be removed when compiling to optimised byte code.
   Severity: Low   Confidence: High
   CWE: CWE-703 (https://cwe.mitre.org/data/definitions/703.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b101_assert_used.html
   Location: src/redrob_ranker/validation.py:33:12
32	        if score == prev_score:
33	            assert cid > prev_cid, f"Tie breaker failed: {cid} should be > {prev_cid}"
34	        assert score <= prev_score, "Score must be non-increasing"

--------------------------------------------------
>> Issue: [B101:assert_used] Use of assert detected. The enclosed code will be removed when compiling to optimised byte code.
   Severity: Low   Confidence: High
   CWE: CWE-703 (https://cwe.mitre.org/data/definitions/703.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b101_assert_used.html
   Location: src/redrob_ranker/validation.py:34:8
33	            assert cid > prev_cid, f"Tie breaker failed: {cid} should be > {prev_cid}"
34	        assert score <= prev_score, "Score must be non-increasing"
35	

--------------------------------------------------
>> Issue: [B101:assert_used] Use of assert detected. The enclosed code will be removed when compiling to optimised byte code.
   Severity: Low   Confidence: High
   CWE: CWE-703 (https://cwe.mitre.org/data/definitions/703.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b101_assert_used.html
   Location: src/redrob_ranker/validation.py:40:8
39	        rank = int(row["rank"])
40	        assert rank == idx + 1, f"Expected rank {idx + 1}, got {rank}"
41	

--------------------------------------------------
>> Issue: [B101:assert_used] Use of assert detected. The enclosed code will be removed when compiling to optimised byte code.
   Severity: Low   Confidence: High
   CWE: CWE-703 (https://cwe.mitre.org/data/definitions/703.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b101_assert_used.html
   Location: src/redrob_ranker/validation.py:42:8
41	
42	        assert row["reasoning"].strip(), "Reasoning is empty"
43	

--------------------------------------------------
>> Issue: [B101:assert_used] Use of assert detected. The enclosed code will be removed when compiling to optimised byte code.
   Severity: Low   Confidence: High
   CWE: CWE-703 (https://cwe.mitre.org/data/definitions/703.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b101_assert_used.html
   Location: src/redrob_ranker/validation.py:53:8
52	    for cid in seen_ids:
53	        assert cid in valid_ids, f"Candidate ID {cid} not found in candidates.jsonl"
54	

--------------------------------------------------

Code scanned:
	Total lines of code: 545
	Total lines skipped (#nosec): 0
	Total potential issues skipped due to specifically being disabled (e.g., #nosec BXXX): 0

Run metrics:
	Total issues (by severity):
		Undefined: 0
		Low: 13
		Medium: 0
		High: 0
	Total issues (by confidence):
		Undefined: 0
		Low: 0
		Medium: 0
		High: 13
Files skipped (0):
## Pip Audit
Found 5 known vulnerabilities in 1 package
Name       Version ID               Fix Versions
---------- ------- ---------------- ------------
setuptools 65.5.0  PYSEC-2022-43012 65.5.1
setuptools 65.5.0  PYSEC-2022-43012 65.5.1
setuptools 65.5.0  PYSEC-2025-49    78.1.1
setuptools 65.5.0  PYSEC-2025-49    78.1.1
setuptools 65.5.0  CVE-2024-6345    70.0.0

Name          Skip Reason
------------- ----------------------------------------------------------------------------
redrob-ranker Dependency not found on PyPI and could not be audited: redrob-ranker (0.1.0)
