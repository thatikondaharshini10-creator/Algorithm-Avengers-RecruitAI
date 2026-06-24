import json
from career_score import calculate_career_score
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from candidate_filter import is_relevant_candidate
from experience_score import calculate_experience_score
from retrieval_score import calculate_retrieval_score

from candidate_builder import build_candidate_text
from behavior_score import calculate_behavior_score

print("Loading model...")
model = SentenceTransformer("all-MiniLM-L6-v2")

print("Loading JD requirements...")

with open("data/jd_requirements.txt", "r", encoding="utf-8") as file:
    jd_text = file.read()

jd_embedding = model.encode(jd_text)

print("Loading candidates...")

with open("sample_candidates.json", "r", encoding="utf-8") as file:
    candidates = json.load(file)

results = []

for candidate in candidates:
    if not is_relevant_candidate(candidate):
     continue
    career_score = calculate_career_score(candidate)
    candidate_text = build_candidate_text(candidate)

    candidate_embedding = model.encode(candidate_text)

    semantic_score = cosine_similarity(
        [jd_embedding],
        [candidate_embedding]
    )[0][0]

    behavior_score = calculate_behavior_score(candidate)
    experience_score = calculate_experience_score(candidate)
    retrieval_score = calculate_retrieval_score(candidate)
    final_score = (
    0.40 * semantic_score +
    0.20 * behavior_score +
    0.15 * career_score +
    0.10 * experience_score +
    0.15 * retrieval_score
)

    results.append({
        "candidate_id": candidate["candidate_id"],
        "semantic_score": semantic_score,
        "behavior_score": behavior_score,
        "experience_score": experience_score,
        "final_score": final_score,
        "career_score": career_score,
        "retrieval_score": retrieval_score
    })

results.sort(
    key=lambda x: x["final_score"],
    reverse=True
)

print("\nTOP 10 CANDIDATES\n")

for candidate in results[:10]:

    print(
        candidate["candidate_id"],
        "| Final:", round(candidate["final_score"], 4),
        "| Semantic:", round(candidate["semantic_score"], 4),
        "| Career:", round(candidate["career_score"], 4),
        "| Experience:", round(candidate["experience_score"], 4),
        "| Behavior:", round(candidate["behavior_score"], 4),
        "| Retrieval:", round(candidate["retrieval_score"], 4)
    )