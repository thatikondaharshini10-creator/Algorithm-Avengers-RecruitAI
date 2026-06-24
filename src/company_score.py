PRODUCT_INDUSTRIES = [
    "software",
    "ai/ml",
    "saas",
    "adtech",
    "fintech",
    "e-commerce",
    "food delivery"
]

SERVICE_INDUSTRIES = [
    "it services",
    "consulting"
]


def calculate_company_score(candidate):

    score = 0.5

    for job in candidate["career_history"]:

        industry = job.get(
            "industry",
            ""
        ).lower()

        if industry in PRODUCT_INDUSTRIES:
            score += 0.15

        if industry in SERVICE_INDUSTRIES:
            score -= 0.05

    score = max(0.0, min(score, 1.0))

    return score