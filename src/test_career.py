import json

from career_score import calculate_career_score

with open("data/sample_candidates.json", "r", encoding="utf-8") as file:
    candidates = json.load(file)

candidate = candidates[30]

print(calculate_career_score(candidate))