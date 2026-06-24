import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )
    )
)
import streamlit as st
import json
import pandas as pd

from src.behavior_score import calculate_behavior_score
from src.career_score import calculate_career_score
from src.experience_score import calculate_experience_score
from src.retrieval_score import calculate_retrieval_score
from src.production_ml_score import calculate_production_ml_score
from src.company_score import calculate_company_score
from src.reasoning_generator import generate_reasoning
from src.honeypot_score import calculate_honeypot_penalty

st.set_page_config(
page_title="RecruitAI",
page_icon="🤖"
)

st.title("RecruitAI")
st.subheader("AI-Powered Candidate Ranking System")

st.write(
"Demo version for Redrob Data & AI Challenge"
)

if st.button("Run Ranking"):

 with open(
     "samples/sample_candidates.json",
     "r",
     encoding="utf-8"
 ) as file:

     candidates = json.load(file)

 results = []

 for candidate in candidates:

     behavior_score = calculate_behavior_score(candidate)

     career_score = calculate_career_score(candidate)

     experience_score = calculate_experience_score(candidate)

     retrieval_score = calculate_retrieval_score(candidate)

     production_ml_score = (
        calculate_production_ml_score(candidate)
     )

     company_score = (
        calculate_company_score(candidate)
     )

     honeypot_penalty = (
        calculate_honeypot_penalty(candidate)
    )

     final_score = (
         0.20 * behavior_score +
         0.20 * career_score +
         0.15 * experience_score +
         0.15 * retrieval_score +
         0.15 * production_ml_score +
         0.15 * company_score
     )

     final_score -= honeypot_penalty

     results.append({
         "candidate_id": candidate["candidate_id"],
         "score": round(final_score, 4),
         "reasoning": generate_reasoning(candidate)
     })

 results.sort(
     key=lambda x: x["score"],
     reverse=True
 )

 for rank, row in enumerate(results, start=1):
     row["rank"] = rank

 df = pd.DataFrame(results)

 st.success("Ranking Complete")

 st.dataframe(
     df[
          [
             "rank",
             "candidate_id",
             "score",
             "reasoning"
         ]
       ]
   )

 csv = df.to_csv(
     index=False
 ).encode("utf-8")

 st.download_button(
     label="Download Ranked CSV",
     data=csv,
     file_name="ranked_candidates.csv",
     mime="text/csv"
   )