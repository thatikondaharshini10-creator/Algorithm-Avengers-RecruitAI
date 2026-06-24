def career_relevance_score(candidate):

    positive_keywords = [
        "ai engineer",
        "ml engineer",
        "machine learning",
        "data scientist",
        "retrieval",
        "ranking",
        "recommendation",
        "search",
        "nlp",
        "embeddings",
        "vector search",
        "llm"
    ]

    negative_keywords = [
        "marketing manager",
        "sales executive",
        "customer support",
        "operations manager",
        "brand design",
        "seo",
        "content marketing"
    ]

    score = 0

    # Check current title
    title = candidate["profile"]["current_title"].lower()

    for word in positive_keywords:
        if word in title:
            score += 5

    for word in negative_keywords:
        if word in title:
            score -= 5

    # Check career history
    for job in candidate["career_history"]:

        text = (
            job["title"] + " " +
            job["description"]
        ).lower()

        for word in positive_keywords:
            if word in text:
                score += 2

        for word in negative_keywords:
            if word in text:
                score -= 2

    return score