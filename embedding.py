from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

chunks = [
    "Priyanshu is a software developer with experience in Python.",
    "He has worked with FastAPI and AI agents.",
    "He has experience with SQL and database integration."
]

embeddings = model.encode(chunks)

print("Number of chunks:", len(chunks))
print("Number of embeddings:", len(embeddings))
print("Size of one embedding:", len(embeddings[0]))