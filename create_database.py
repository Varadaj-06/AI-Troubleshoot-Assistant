
import json
import chromadb
from sentence_transformers import SentenceTransformer

# Load knowledge base
with open("knowledge_base.json", "r", encoding="utf-8") as file:
    knowledge_base = json.load(file)

# Load embedding model
print("Loading embedding model...")

model = SentenceTransformer("all-MiniLM-L6-v2")

# Create ChromaDB client
client = chromadb.PersistentClient(path="./chroma_db")

# Create collection
collection = client.get_or_create_collection(
    name="troubleshooting_knowledge"
)

# Prepare documents
documents = []
ids = []
metadatas = []

for entry in knowledge_base:

    text = f"""
    Issue: {entry['issue']}
    Category: {entry['category']}
    Symptoms: {', '.join(entry['symptoms'])}
    Diagnostic Checks: {', '.join(entry['diagnostic_checks'])}
    Resolution Steps: {', '.join(entry['resolution_steps'])}
    Escalation Team: {entry['escalation_team']}
    Escalation Condition: {entry['escalation_condition']}
    """

    documents.append(text)
    ids.append(entry["id"])

    metadatas.append({
        "issue": entry["issue"],
        "category": entry["category"],
        "escalation_team": entry["escalation_team"]
    })

# Generate embeddings
print("Generating embeddings...")

embeddings = model.encode(documents).tolist()

# Store in ChromaDB
collection.upsert(
    ids=ids,
    documents=documents,
    embeddings=embeddings,
    metadatas=metadatas
)

print("Knowledge base successfully stored!")
print("Total documents:", collection.count())