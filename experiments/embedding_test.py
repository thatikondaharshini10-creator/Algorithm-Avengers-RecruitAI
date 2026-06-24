from sentence_transformers import SentenceTransformer

print("Loading model...")

model = SentenceTransformer("all-MiniLM-L6-v2")

print("Model loaded successfully!")

text = """
Backend Engineer
Python
SQL
Spark
"""

embedding = model.encode(text)

print("Embedding Length:", len(embedding))
print("First 10 values:")
print(embedding[:10])