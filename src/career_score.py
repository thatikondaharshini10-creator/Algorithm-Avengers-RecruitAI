def calculate_career_score(candidate):

    title = candidate["profile"]["current_title"].lower()

    # Tier A: Perfect Match
    tier_a = [
        "recommendation systems engineer",
        "search engineer",
        "nlp engineer",
        "applied ml engineer"
    ]

    # Tier B: Strong Match
    tier_b = [
        "ml engineer",
        "ai research engineer",
        "data scientist"
    ]

    # Tier C: Adjacent Match
    tier_c = [
        "data engineer",
        "analytics engineer",
        "backend engineer"
    ]

    # Tier D: Generic Engineering
    tier_d = [
        "software engineer",
        "full stack developer",
        "cloud engineer",
        "devops engineer",
        "java developer",
        "frontend engineer"
    ]

    for role in tier_a:
        if role in title:
            return 1.0

    for role in tier_b:
        if role in title:
            return 0.9

    for role in tier_c:
        if role in title:
            return 0.7

    for role in tier_d:
        if role in title:
            return 0.5

    return 0.1