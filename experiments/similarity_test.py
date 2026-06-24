from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("all-MiniLM-L6-v2")

jd = """
Senior AI Engineer

Need experience in:
embeddings
retrieval
ranking systems
vector databases
Python
"""

candidate = """
Backend Engineer

Skills:
Python
SQL
Spark
Milvus
Fine-tuning LLMs

Built data pipelines using Spark.
Worked with ML teams.
"""

jd_embedding = model.encode(jd)

candidate_embedding = model.encode(candidate)

score = cosine_similarity(
    [jd_embedding],
    [candidate_embedding]
)

print("Similarity Score:")
print(score)