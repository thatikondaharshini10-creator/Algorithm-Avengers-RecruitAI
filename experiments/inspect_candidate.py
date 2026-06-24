import json
from pprint import pprint

target_id = "CAND_0004989"

with open("samples/sample_candidates.json", "r", encoding="utf-8") as file:
    candidates = json.load(file)

found = False

for candidate in candidates:

    if candidate["candidate_id"] == target_id:
        pprint(candidate)
        found = True
        break

if not found:
    print("Candidate not found!")