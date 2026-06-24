import json
import csv
import time

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

from candidate_builder import build_candidate_text
from candidate_filter import is_relevant_candidate

from behavior_score import calculate_behavior_score
from career_score import calculate_career_score
from experience_score import calculate_experience_score
from retrieval_score import calculate_retrieval_score
from production_ml_score import calculate_production_ml_score
from company_score import calculate_company_score

from reasoning_generator import generate_reasoning


print("Loading model...")
model = SentenceTransformer("all-MiniLM-L6-v2")

print("Loading JD...")

with open("data/job_description.txt", "r", encoding="utf-8") as file:
    jd_text = file.read()

jd_embedding = model.encode(jd_text)

results = []

processed = 0
kept = 0

start_time = time.time()

print("Processing candidates...")

with open("data/candidates.jsonl", "r", encoding="utf-8") as file:

    for line in file:

        processed += 1

        candidate = json.loads(line)

        if not is_relevant_candidate(candidate):
            continue

        kept += 1

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

        production_ml_score = (
            calculate_production_ml_score(candidate)
        )

        company_score = (
            calculate_company_score(candidate)
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

        reasoning = generate_reasoning(candidate)

        results.append({
            "candidate_id": candidate["candidate_id"],
            "score": round(final_score, 4),
            "reasoning": reasoning
        })

        if processed % 5000 == 0:
            print(
                f"Processed: {processed} | "
                f"Relevant: {kept}"
            )

print("\nSorting candidates...")

results.sort(
    key=lambda x: x["score"],
    reverse=True
)

print("Writing CSV...")

with open(
    "ranked_candidates.csv",
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

    rank = 1

    for candidate in results:

        writer.writerow([
            candidate["candidate_id"],
            rank,
            candidate["score"],
            candidate["reasoning"]
        ])

        rank += 1

end_time = time.time()

print("\nDone!")
print("Candidates Ranked:", len(results))
print(
    "Total Time:",
    round(end_time - start_time, 2),
    "seconds"
)
print("Output File: ranked_candidates.csv")