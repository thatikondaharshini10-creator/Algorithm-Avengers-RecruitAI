import json
import numpy as np
from sentence_transformers import SentenceTransformer

from candidate_builder import build_candidate_text
from candidate_filter import is_relevant_candidate

print("Loading model...")
model = SentenceTransformer("all-MiniLM-L6-v2")

candidate_ids = []
candidate_texts = []

print("Loading candidates...")

with open("data/candidates.jsonl", "r", encoding="utf-8") as file:

    for line in file:

        candidate = json.loads(line)

        if not is_relevant_candidate(candidate):
            continue

        candidate_ids.append(candidate["candidate_id"])

        candidate_texts.append(
            build_candidate_text(candidate)
        )

print("Relevant Candidates:", len(candidate_ids))

print("Generating embeddings...")

embeddings = model.encode(
    candidate_texts,
    batch_size=64,
    show_progress_bar=True,
    convert_to_numpy=True
)

print("Saving embeddings...")

np.save(
    "artifacts/candidate_embeddings.npy",
    embeddings
)

with open(
    "artifacts/candidate_ids.json",
    "w",
    encoding="utf-8"
) as file:

    json.dump(candidate_ids, file)

print("Done!")
print("Embeddings Shape:", embeddings.shape)