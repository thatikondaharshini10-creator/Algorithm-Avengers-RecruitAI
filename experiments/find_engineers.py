import json

with open("sample_candidates.json", "r", encoding="utf-8") as f:
    candidates = json.load(f)

for c in candidates:

    title = c["profile"]["current_title"].lower()

    if (
        "engineer" in title
        or "scientist" in title
        or "developer" in title
        or "ml" in title
        or "ai" in title
    ):
        print(
            c["candidate_id"],
            "|",
            c["profile"]["current_title"],
            "|",
            c["profile"]["years_of_experience"]
        )
        