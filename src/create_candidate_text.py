import json

with open("data/sample_candidates.json", "r", encoding="utf-8") as file:
    data = json.load(file)

candidate = data[0]

profile = candidate["profile"]

print(profile["headline"])
print(profile["summary"])