import json

from candidate_builder import build_candidate_text

with open("samples/sample_candidates.json", "r", encoding="utf-8") as file:
    candidates = json.load(file)

candidate = candidates[30]

text = build_candidate_text(candidate)

print(text)