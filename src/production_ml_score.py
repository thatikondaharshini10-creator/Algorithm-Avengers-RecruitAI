STRONG_SIGNALS = [
    "built recommendation",
    "recommendation system",
    "ranking model",
    "ranking models",
    "retrieval system",
    "search product",
    "search platform",
    "learning-to-rank",
    "evaluation pipeline",
    "offline-online correlation",
    "a/b test",
    "ab test",
    "re-ranking",
    "engagement signals",
    "click-through"
]

MEDIUM_SIGNALS = [
    "recommendation",
    "ranking",
    "retrieval",
    "search",
    "embeddings",
    "evaluation",
    "xgboost"
]


def calculate_production_ml_score(candidate):

    text = ""

    for job in candidate["career_history"]:
        text += job.get("description", "").lower() + " "

    score = 0

    for signal in STRONG_SIGNALS:

        if signal in text:
            score += 2

    for signal in MEDIUM_SIGNALS:

        if signal in text:
            score += 1

    return min(score / 12, 1.0)