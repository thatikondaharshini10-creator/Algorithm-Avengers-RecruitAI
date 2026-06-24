import json
import csv
import numpy as np
import time

start_time = time.time()

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

from behavior_score import calculate_behavior_score
from career_score import calculate_career_score
from experience_score import calculate_experience_score
from retrieval_score import calculate_retrieval_score
from production_ml_score import calculate_production_ml_score
from company_score import calculate_company_score
from reasoning_generator import generate_reasoning
from honeypot_score import calculate_honeypot_penalty

print("Loading model...")
model = SentenceTransformer("all-MiniLM-L6-v2")

print("Loading JD...")

with open("data/job_description.txt", "r", encoding="utf-8") as file:
    jd_text = file.read()

jd_embedding = model.encode(jd_text)

print("Loading embeddings...")

candidate_embeddings = np.load(
    "artifacts/candidate_embeddings.npy"
)

with open(
    "artifacts/candidate_ids.json",
    "r",
    encoding="utf-8"
) as file:
    candidate_ids = json.load(file)

print("Computing similarities...")

similarities = cosine_similarity(
    [jd_embedding],
    candidate_embeddings
)[0]

print("Selecting Top 2000 semantic matches...")

top_indices = np.argsort(similarities)[::-1][:2000]

candidate_lookup = {}

print("Loading candidates...")

with open(
    "data/candidates.jsonl",
    "r",
    encoding="utf-8"
) as file:

    for line in file:

        candidate = json.loads(line)

        candidate_lookup[
            candidate["candidate_id"]
        ] = candidate

results = []

print("Calculating final scores...")

for idx in top_indices:

    candidate_id = candidate_ids[idx]

    candidate = candidate_lookup[candidate_id]

    semantic_score = float(similarities[idx])

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
        0.25 * semantic_score +
        0.15 * behavior_score +
        0.15 * career_score +
        0.10 * experience_score +
        0.15 * retrieval_score +
        0.10 * production_ml_score +
        0.10 * company_score
    )
    final_score -= honeypot_penalty

    reasoning = generate_reasoning(candidate)

    results.append({
        "candidate_id": candidate_id,
        "score": round(final_score, 4),
        "reasoning": reasoning
    })

results.sort(
    key=lambda x: x["score"],
    reverse=True
)
candidate_ids_check = [
    row["candidate_id"]
    for row in results[:100]
]

if len(candidate_ids_check) != len(set(candidate_ids_check)):
    print("ERROR: Duplicate candidate IDs found!")
    exit()
print("Writing Top 100...")

with open(
    "output/ranked_candidates_top100.csv",
    "w",
    newline="",
    encoding="utf-8"
) as csvfile:

    writer = csv.writer(csvfile)

    writer.writerow([
        "candidate_id",
        "rank",
        "score",
        "reasoning"
    ])

    for rank, candidate in enumerate(
        results[:100],
        start=1
    ):

        writer.writerow([
            candidate["candidate_id"],
            rank,
            candidate["score"],
            candidate["reasoning"]
        ])
top100 = results[:100]

# Check 1

if len(top100) != 100:
    print("ERROR: Not exactly 100 candidates")
    exit()

# Check 2

ids = [
    c["candidate_id"]
    for c in top100
]

if len(ids) != len(set(ids)):
    print("ERROR: Duplicate candidate IDs")
    exit()

# Check 3

scores = [
    c["score"]
    for c in top100
]

if len(set(scores)) == 1:
    print("ERROR: All scores identical")
    exit()

# Check 4

for i in range(len(scores)-1):

    if scores[i] < scores[i+1]:

        print(
            "ERROR: Scores not sorted"
        )

        exit()

print("Validation Passed")
print("Done!")
print("Top 100 exported.")
end_time = time.time()

print("Runtime:", round(end_time - start_time, 2), "seconds")