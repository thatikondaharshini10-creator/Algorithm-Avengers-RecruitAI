import json
from collections import Counter

important_titles = [
    "ML Engineer",
    "AI Research Engineer",
    "Data Scientist",
    "Data Engineer",
    "Backend Engineer",
    "Analytics Engineer",
    "Software Engineer",
    "Full Stack Developer",
    "Cloud Engineer",
    "DevOps Engineer",
    "Java Developer",
    "Frontend Engineer",
    "Recommendation Systems Engineer",
    "Search Engineer",
    "NLP Engineer",
    "Applied ML Engineer"
]

counter = Counter()

with open("data/candidates.jsonl", "r", encoding="utf-8") as file:

    for line in file:

        candidate = json.loads(line)

        title = candidate["profile"]["current_title"]

        if title in important_titles:
            counter[title] += 1

print("\nIMPORTANT TITLE COUNTS\n")

for title in important_titles:
    print(title, "->", counter[title])