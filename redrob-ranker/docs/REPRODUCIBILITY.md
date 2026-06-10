# REPRODUCIBILITY

This ranking engine is 100% deterministic and uses no stochastic LLM endpoints during the inference path.

Runtime expectations:
- ~12-15 seconds for 100,000 JSONL records on a standard vCPU.
- Peak Memory: < 150MB since data is streamed sequentially.

**Steps to Repro**:
1. Unzip the competition dataset to `data/`.
2. Run `make install` to configure dependencies.
3. Run `make rank`.
4. The output will be inside the `submissions/` directory. 
