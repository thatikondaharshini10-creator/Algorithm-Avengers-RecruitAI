import json
from collections import Counter

title_counter = Counter()
skill_counter = Counter()
industry_counter = Counter()

total = 0

with open("data/candidates.jsonl", "r", encoding="utf-8") as file:

    for line in file:

        candidate = json.loads(line)

        total += 1

        # Title
        title = candidate["profile"]["current_title"]
        title_counter[title] += 1

        # Industry
        industry = candidate["profile"]["current_industry"]
        industry_counter[industry] += 1

        # Skills
        for skill in candidate["skills"]:
            skill_counter[skill["name"]] += 1

print("\nTOTAL CANDIDATES:")
print(total)

print("\nTOP 30 TITLES:")
for title, count in title_counter.most_common(30):
    print(title, "->", count)

print("\nTOP 30 INDUSTRIES:")
for industry, count in industry_counter.most_common(30):
    print(industry, "->", count)

print("\nTOP 50 SKILLS:")
for skill, count in skill_counter.most_common(50):
    print(skill, "->", count)