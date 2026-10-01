import chromadb
from sentence_transformers import SentenceTransformer

# 1. Connect to existing ChromaDB
client = chromadb.PersistentClient(path="./chroma_db")

# 2. Get the existing collection
collection = client.get_collection(name="resume")

# 3. Load the same embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

print("=" * 50)
print("          PDF Q&A RAG AGENT")
print("=" * 50)

# 4. Keep asking questions
while True:

    # Take question from user
    question = input("\nYou: ")

    # Exit the program
    if question.lower() == "exit":
        print("Bot: Goodbye!")
        break

    # 5. Convert question into embedding
    question_embedding = model.encode(question)

    # 6. Search ChromaDB
    results = collection.query(
        query_embeddings=[question_embedding.tolist()],
        n_results=2
    )

    # 7. Display relevant information
    print("\nRelevant information:")

    for i, document in enumerate(results["documents"][0]):
        print(f"\n--- Result {i + 1} ---")
        print(document)

    print("\n" + "-" * 50)
