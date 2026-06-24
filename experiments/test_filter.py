import json

from candidate_filter import is_relevant_candidate

count = 0

with open("data/candidates.jsonl", "r", encoding="utf-8") as file:

    for line in file:

        candidate = json.loads(line)

        if is_relevant_candidate(candidate):
            count += 1

print("Relevant Candidates:", count)