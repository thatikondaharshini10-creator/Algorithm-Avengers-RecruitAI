import json

TARGET_TITLES = {
    "Recommendation Systems Engineer",
    "Search Engineer",
    "NLP Engineer",
    "Applied ML Engineer",
    "ML Engineer",
    "AI Research Engineer"
}

current_count = 0
history_count = 0

with open("data/candidates.jsonl", "r", encoding="utf-8") as file:

    for line in file:

        candidate = json.loads(line)

        current_title = candidate["profile"]["current_title"]

        if current_title in TARGET_TITLES:
            current_count += 1

        found_in_history = False

        for job in candidate["career_history"]:

            if job["title"] in TARGET_TITLES:
                found_in_history = True
                break

        if found_in_history:
            history_count += 1

print("\nCurrent Title Matches:", current_count)
print("Career History Matches:", history_count)