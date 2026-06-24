import json

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

from candidate_builder import build_candidate_text

print("Loading model...")
model = SentenceTransformer("all-MiniLM-L6-v2")

# Load JD
with open("data/jd_requirements.txt", "r", encoding="utf-8") as file:
    jd_text = file.read()

jd_embedding = model.encode(jd_text)

# Load candidates
with open("samples/sample_candidates.json", "r", encoding="utf-8") as file:
    candidates = json.load(file)

# Candidate 14
candidate = candidates[30]

candidate_text = build_candidate_text(candidate)

candidate_embedding = model.encode(candidate_text)

score = cosine_similarity(
    [jd_embedding],
    [candidate_embedding]
)[0][0]

print("\nSemantic Score:")
print(score)