
import chromadb
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_collection(
    name="troubleshooting_knowledge"
)

def retrieve_knowledge(question, top_k=2):

    question_embedding = model.encode(question).tolist()

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

#retriever testing
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
