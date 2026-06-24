count = 0

with open("data/candidates.jsonl", "r", encoding="utf-8") as file:
    for line in file:
        count += 1

print("Total Candidates:", count)