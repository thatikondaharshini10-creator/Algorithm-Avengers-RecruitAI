import json
from pprint import pprint

target_id = "CAND_0031513"

with open("data/candidates.jsonl", "r", encoding="utf-8") as file:

    for line in file:

        candidate = json.loads(line)

        if candidate["candidate_id"] == target_id:

            pprint(candidate)

            break