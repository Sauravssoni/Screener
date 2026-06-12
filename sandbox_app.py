import streamlit as st
import json
import pandas as pd
from io import StringIO

from src.redrob_ranker.agents.ranking_agent import rank_candidates
from src.redrob_ranker.features import extract_features, detect_traps

st.set_page_config(page_title="RedrobRank Sandbox", layout="wide")

st.title("RedrobRank Agentic Recruiter OS - Sandbox")
st.markdown("""
**Note:** Full 100K ranking is run via CLI; this sandbox is for small-sample reproducibility and demonstration.
This sandbox runs entirely locally and makes no external API calls.
""")

uploaded_file = st.file_uploader("Upload a small candidates.jsonl file (max 1000 lines)", type=["jsonl"])

if uploaded_file is not None:
    content = uploaded_file.getvalue().decode("utf-8")
    lines = content.strip().split('\n')
    
    if len(lines) > 1000:
        st.warning(f"File too large ({len(lines)} lines). Truncating to 1000 for browser sandbox.")
        lines = lines[:1000]
        
    st.info(f"Loaded {len(lines)} candidates.")
    
    if st.button("Run Deterministic Ranker"):
        candidates_with_context = []
        
        with st.spinner("Extracting features and scoring..."):
            for line in lines:
                if not line.strip():
                    continue
                try:
                    c = json.loads(line)
                    features = extract_features(c)
                    traps = detect_traps(c, features)
                    candidates_with_context.append((c, features, traps, None))
                except Exception as e:
                    st.error(f"Error parsing line: {e}")
                    
            scored_candidates = rank_candidates(candidates_with_context)
            
            # Format output for table
            table_data = []
            for idx, c in enumerate(scored_candidates):
                prof = c.get("profile", {})
                table_data.append({
                    "Rank": idx + 1,
                    "Candidate ID": c.get("candidate_id"),
                    "Title": prof.get("current_title"),
                    "YOE": prof.get("years_of_experience"),
                    "Score": round(c.get("final_score", 0), 4),
                    "Reasoning": c.get("reasoning", "")
                })
                
            df = pd.DataFrame(table_data)
            st.success("Ranking Complete!")
            st.dataframe(df, use_container_width=True)
            
            csv = df.to_csv(index=False)
            st.download_button(
                label="Download Ranked CSV",
                data=csv,
                file_name='sandbox_submission.csv',
                mime='text/csv',
            )
else:
    st.write("Please upload a .jsonl file to test the deterministic ranking engine.")
