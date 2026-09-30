import pymupdf
from sentence_transformers import SentenceTransformer
import chromadb

# 1. Open PDF
pdf = pymupdf.open("documents/PY.Resume.pdf")

# 2. Extract all text
text = ""

for page in pdf:
    text += page.get_text()

pdf.close()

# 3. Create chunks
chunk_size = 500
chunks = []

for i in range(0, len(text), chunk_size):
    chunk = text[i:i + chunk_size]
    chunks.append(chunk)

print("Number of chunks:", len(chunks))

# 4. Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# 5. Create embeddings
embeddings = model.encode(chunks)

print("Number of embeddings:", len(embeddings))

# 6. Create ChromaDB client
client = chromadb.PersistentClient(path="./chroma_db")

# 7. Create collection
collection = client.get_or_create_collection(name="resume")

# 8. Store chunks and embeddings
collection.add(
    ids=[str(i) for i in range(len(chunks))],
    documents=chunks,
    embeddings=embeddings.tolist()
)

print("Data stored in ChromaDB!")