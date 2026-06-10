# Assumptions

1. **Processing Capability**: Assumed no heavy LLM use during ranking step to respect the 5-minute CPU-only constraints.
2. **Text Normalization**: Simple tokenization handles comma-separated keyword matching.
3. **Data Completeness**: Allowed handling for missing data by using safe `.get()` dict accesses.
4. **Keyword Proxies**: Used BM25, ANN, Pinecone as proxies for candidate capabilities around similarity search, even if not phrased as "vector search".
