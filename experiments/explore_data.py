import json
from pprint import pprint

with open("samples/sample_candidates.json", "r", encoding="utf-8") as file:
    data = json.load(file)

print("Total Candidates:", len(data))

print("\n===== FIRST CANDIDATE =====\n")

pprint(data[0])