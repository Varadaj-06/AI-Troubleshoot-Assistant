
import chromadb
from sentence_transformers import SentenceTransformer

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Connect to existing ChromaDB
client = chromadb.PersistentClient(path="./chroma_db")

# Access collection
collection = client.get_collection(
    name="troubleshooting_knowledge"
)

def retrieve_knowledge(question, top_k=2):

    # Convert user question into embedding
    question_embedding = model.encode(question).tolist()

    # Search for similar documents
    results = collection.query(
        query_embeddings=[question_embedding],
        n_results=top_k
    )

    retrieved_documents = []

    for i in range(len(results["ids"][0])):

        retrieved_documents.append({
            "id": results["ids"][0][i],
            "document": results["documents"][0][i],
            "metadata": results["metadatas"][0][i],
            "distance": results["distances"][0][i]
        })

    return retrieved_documents

# Test the retriever
if __name__ == "__main__":

    question = "Payment failed. Should I try charging the customer again?"

    results = retrieve_knowledge(question)

    print("\nUser Question:", question)

    print("\nRetrieved Knowledge:")

    for result in results:
        print("\nID:", result["id"])
        print("Issue:", result["metadata"]["issue"])
        print("Category:", result["metadata"]["category"])
        print("Distance:", result["distance"])
        print("Details:", result["document"])