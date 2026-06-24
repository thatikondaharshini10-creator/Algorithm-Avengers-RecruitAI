KEYWORDS = [
    "retrieval",
    "ranking",
    "search",
    "recommendation",
    "recommendation system",
    "embeddings",
    "vector",
    "faiss",
    "pinecone",
    "milvus",
    "weaviate",
    "information retrieval",
    "re-ranking",
    "ndcg",
    "mrr",
    "ab testing",
    "a/b testing"
]


def calculate_retrieval_score(candidate):

    score = 0

    text = ""

    for job in candidate["career_history"]:
        text += job["description"].lower() + " "

    for skill in candidate["skills"]:
        text += skill["name"].lower() + " "

    for keyword in KEYWORDS:

        if keyword in text:
            score += 1

    return min(score / 10, 1.0)