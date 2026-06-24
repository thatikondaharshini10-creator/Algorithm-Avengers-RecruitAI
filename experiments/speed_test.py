import json
import time

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

from candidate_builder import build_candidate_text
from behavior_score import calculate_behavior_score
from career_score import calculate_career_score
from experience_score import calculate_experience_score
from retrieval_score import calculate_retrieval_score
from candidate_filter import is_relevant_candidate

print("Loading model...")
model = SentenceTransformer("all-MiniLM-L6-v2")

# Load JD
with open("data/job_description.txt", "r", encoding="utf-8") as file:
    jd_text = file.read()

jd_embedding = model.encode(jd_text)

print("Loading candidates...")

start_time = time.time()

processed = 0

with open("data/candidates.jsonl", "r", encoding="utf-8") as file:

    for line in file:

        candidate = json.loads(line)

        if not is_relevant_candidate(candidate):
            continue

        candidate_text = build_candidate_text(candidate)

        candidate_embedding = model.encode(candidate_text)

        semantic_score = cosine_similarity(
            [jd_embedding],
            [candidate_embedding]
        )[0][0]

        behavior_score = calculate_behavior_score(candidate)
        career_score = calculate_career_score(candidate)
        experience_score = calculate_experience_score(candidate)
        retrieval_score = calculate_retrieval_score(candidate)

        final_score = (
            0.40 * semantic_score +
            0.20 * behavior_score +
            0.15 * career_score +
            0.10 * experience_score +
            0.15 * retrieval_score
        )

        processed += 1

        if processed == 100:
            break

end_time = time.time()

print("\nRESULTS")
print("Candidates Processed:", processed)
print("Time Taken:", round(end_time - start_time, 2), "seconds")
print("Average Per Candidate:",
      round((end_time - start_time) / processed, 4),
      "seconds")