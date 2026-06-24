import json

from behavior_score import calculate_behavior_score

with open("samples/sample_candidates.json", "r", encoding="utf-8") as file:
    candidates = json.load(file)

candidate = candidates[30]

score = calculate_behavior_score(candidate)

print("Behavior Score:", score)