# AI Troubleshooting Assistant for L1/L2 Support

## 1. Project Overview

The AI Troubleshooting Assistant is a Python-based application designed to help L1/L2 technical support engineers identify common technical issues and find relevant troubleshooting guidance.

Users can describe problems in natural language. The application searches a predefined knowledge base, retrieves relevant troubleshooting information, and uses Google's Gemini model to generate structured, step-by-step guidance.

The assistant also identifies the appropriate escalation team and displays the knowledge-base sources used to generate its response.

## 2. Objectives

- Build a searchable knowledge base containing common technical issues.
- Retrieve relevant troubleshooting information using semantic search.
- Generate clear troubleshooting instructions using a generative AI model.
- Identify appropriate escalation teams and escalation conditions.
- Display the knowledge sources used for each response.
- Handle unsupported queries without generating misleading solutions.
- Apply basic privacy and security safeguards.

## 3. Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core application development |
| Streamlit | Interactive web interface |
| Google Gemini API | AI-powered response generation |
| Sentence Transformers | Text embedding generation |
| all-MiniLM-L6-v2 | Embedding model |
| ChromaDB | Vector database and semantic retrieval |
| JSON | Knowledge-base storage |

## 4. Knowledge Base

The application uses a structured JSON knowledge base containing 20 simulated technical troubleshooting scenarios.

Each entry includes:

- Issue ID
- Issue description
- Category
- Symptoms
- Diagnostic checks
- Resolution steps
- Escalation team
- Escalation condition

The knowledge base covers payment issues, API errors, database problems, authentication failures, infrastructure issues and network connectivity.

## 5. System Architecture

The application follows a Retrieval-Augmented Generation (RAG) approach.

### Workflow

1. **User Input:** The support engineer enters a technical issue through the Streamlit interface.
2. **Query Embedding:** Sentence Transformers converts the query into a numerical vector.
3. **Semantic Retrieval:** ChromaDB searches the stored embeddings and retrieves the two nearest knowledge-base entries.
4. **Relevance Filtering:** Retrieved entries are filtered using a distance threshold of 1.0.
5. **Context Preparation:** Relevant knowledge-base information is passed to Gemini as context.
6. **AI Response Generation:** Gemini generates structured troubleshooting guidance using the retrieved information.
7. **Response Streaming:** The generated response is displayed progressively in the chat interface.
8. **Source Display:** The application displays the relevant knowledge-base entries used for the response.

If no retrieved entry satisfies the relevance threshold, the application returns an unsupported-query message instead of generating an answer from unrelated information.

## 6. AI Model and Prompt Engineering

### Embedding Model

**all-MiniLM-L6-v2**

Used to convert user queries and knowledge-base documents into vector representations for semantic similarity search.

### Generative AI Model

**Gemini 3.1 Flash-Lite**

Used to generate natural-language troubleshooting responses based on the retrieved knowledge.

### Prompt Engineering

The prompt instructs Gemini to:

- Use only the retrieved knowledge.
- Avoid inventing technical facts or resolutions.
- Provide numbered diagnostic steps.
- Include resolution guidance supported by the knowledge base.
- Identify escalation teams and escalation conditions.
- Request clarification when information is insufficient.
- Avoid claiming that an issue has been resolved without confirmation.
- Protect sensitive information and avoid requesting confidential credentials.
- Avoid claiming access to external systems or actions that the prototype cannot perform.

## 7. Project Structure

```text
AI_Troubleshoot_Assistant/
│
├── app.py
├── assistant.py
├── retriever.py
├── create_database.py
├── knowledge_base.json
├── config.py
├── requirements.txt
├── .gitignore
│
├── .streamlit/
│   └── config.toml
│
└── chroma_db/
```

The `chroma_db` directory is generated when the knowledge base is indexed.

## 8. Installation and Setup

### Prerequisites

- Python installed
- Google Gemini API key
- Internet connection for API access and initial model downloads

### Step 1: Clone or download the project

Navigate to the project directory:

```bash
cd AI_Troubleshoot_Assistant
```

### Step 2: Create a virtual environment

```bash
python -m venv myenv
```

Activate it on Windows PowerShell:

```powershell
.\myenv\Scripts\Activate.ps1
```

### Step 3: Install dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Configure the Gemini API key

Create or update `config.py`:

```python
GEMINI_API_KEY = "YOUR_GEMINI_API_KEY"
```

Replace the placeholder with your own API key. Never upload this file or expose the key publicly.

### Step 5: Build the vector database

```bash
python create_database.py
```

This generates embeddings for the 20 knowledge-base entries and stores them in ChromaDB.

### Step 6: Run the application

```bash
streamlit run app.py
```

Open the local Streamlit URL displayed in the terminal, usually:

```text
http://localhost:8501
```

## 9. Testing and Validation

The application was tested using supported, ambiguous, unsupported and security-related queries.

| Test scenario | Expected behaviour | Observed result |
|---|---|---|
| HTTP 401 Unauthorized | Retrieve relevant API entry | Correct match: KB010 |
| Duplicate payment | Retrieve duplicate-payment guidance | Correct match: KB008 |
| Database connection failure | Retrieve database entry | Correct match: KB002 |
| Low server disk space | Retrieve infrastructure entry | Correct match: KB018 |
| Unsupported laptop screen issue | Reject irrelevant matches | Correctly rejected |
| Ambiguous payment query | Identify pending payment issue | Correct match: KB009 |
| Payment retry question | Provide duplicate-charge prevention guidance | Correct match: KB007 |
| Prompt injection attempt | Avoid revealing secrets or bypass instructions | No secret or bypass instructions provided |

### Retrieval Threshold

The application uses a distance threshold of 1.0.

Results with a distance less than or equal to 1.0 are considered sufficiently relevant for this prototype.

The threshold was evaluated using sample queries. It is a heuristic and may require further calibration with a larger test dataset.

## 10. Assumptions

- The knowledge base contains simulated technical support scenarios.
- The application uses a predefined collection of troubleshooting procedures.
- Gemini is used for response generation, not as the source of technical truth.
- The application does not connect to actual payment gateways, production databases or monitoring systems.
- Escalation recommendations are based on the predefined knowledge base.
- Support engineers are responsible for verifying recommended actions through authorized systems.

## 11. Limitations

- The application can only provide guidance for issues covered by its knowledge base.
- Retrieval accuracy depends on the quality and coverage of knowledge-base entries.
- The distance threshold is heuristic and may reject some relevant queries or accept borderline matches.
- AI-generated responses may require human verification.
- The application does not execute troubleshooting operations or modify production systems.
- Response generation depends on Gemini API availability, connectivity and applicable usage quotas.
- The current prototype does not include authentication, role-based access control or integration with a live ticketing system.

## 12. Future Enhancements

- Expand the knowledge base with more technical support scenarios.
- Improve retrieval accuracy through additional evaluation and threshold calibration.
- Integrate with ticket management systems.
- Add support for uploading troubleshooting documents.
- Introduce user authentication and role-based access.
- Add feedback collection to evaluate answer quality.
- Integrate with monitoring systems for automated diagnostic information.

## 13. Conclusion

The AI Troubleshooting Assistant demonstrates how semantic search and generative AI can be combined to support technical troubleshooting workflows.

By retrieving relevant knowledge before generating responses, the application aims to provide structured, source-grounded guidance while reducing unsupported AI-generated recommendations.

The prototype demonstrates practical applications of Retrieval-Augmented Generation, prompt engineering, semantic search, response streaming and responsible AI practices in an L1/L2 support environment.

---

**Project:** AI Troubleshooting Assistant for L1/L2 Support  
**Developed using:** Python, Streamlit, ChromaDB, Sentence Transformers and Google Gemini API  
**Knowledge Base:** 20 simulated troubleshooting entries