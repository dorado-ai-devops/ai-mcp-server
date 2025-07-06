# 🧠 ai-mcp-server

> FastAPI microservice for registering and storing structured MCP messages (Pipeline Context Messages), connecting Jenkins, AI, and dashboards in a reflexive system.

Built in Python + FastAPI, fully local and deployed via Helm + ArgoCD.

---

## 🚀 Features

- ✅ Registers MCP messages (origin, type, timestamp, microservice, prompt, AI response, etc.)
- 🧠 Each message includes a unique `UUID` + full traceability
- 🗂️ Automatically stores as JSON (`/mnt/data/mcp/`) with versioned filenames
- 📁 Compatible with Streamlit dashboards and CI visualization
- 🧩 POST-based REST API with Pydantic validation
- 🐳 Dockerized and deployable in Kubernetes (Kind + ArgoCD)

---

## 📦 Project Structure

```
ai-mcp-server/
├── main.py                # FastAPI entry point and router
├── models.py              # MCPMessage schemas (Pydantic)
├── routes/
│   └── register.py        # Main endpoint POST /mcp/register
├── services/
│   └── writer.py          # Logic for storing MCP messages as JSON
├── requirements.txt       # Python dependencies
├── Dockerfile             # Container image definition
├── Makefile               # Automated build and deployment
└── README.md              # Project documentation
```

---

## 🧩 Components

### `routes/register.py`

Defines the main REST endpoint:

```
POST /mcp/register
```

- Expected input: JSON with fields `source`, `type`, `microservice`, `timestamp`, `prompt_path`, etc.
- Validates the message with Pydantic and saves it to disk (`/mnt/data/mcp/`)

---

## 🧠 Internal Logic

### `models.py`

Defines the MCPMessage model:

- Fields: `id`, `source`, `type`, `timestamp`, `tags`, `summary`, etc.
- `id` is automatically generated as a UUID (`uuid4`)

### `writer.py`

- Builds a unique filename with `timestamp + UUID`
- Saves the message as readable JSON (UTF-8, indented)
- Fully compatible with future indexers (e.g., SQLite) or dashboards

---

## 🔁 Jenkins Integration

From any Jenkins pipeline you can call:

```bash
curl -X POST http://ai-mcp-server.devops-ai.svc.cluster.local:8001/mcp/register \
  -H "Content-Type: application/json" \
  -d '{
    "source": "jenkins",
    "type": "pipeline-execution",
    "microservice": "ai-log-analyzer",
    "prompt_path": "/mnt/data/gateway/test.prompt",
    "response_path": "/mnt/data/gateway/response.json",
    "llm_used": "ollama-mistral-7b",
    "timestamp": "2025-07-05T22:20:00",
    "summary": "Automated analysis completed successfully.",
    "tags": ["jenkins", "logs", "ai"]
}'
```

---

## 🛠️ Getting Started (Local)

```bash
git clone git@github.com:dorado-ai-devops/ai-mcp-server.git
cd ai-mcp-server
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Run locally

```bash
uvicorn main:app --reload --port 8001
```

---

## 💾 Example Stored Message

```json
{
  "id": "bf11c2b3-21c2-4c9b-81f2-e8077f80e937",
  "source": "jenkins",
  "type": "pipeline-execution",
  "microservice": "ai-log-analyzer",
  "prompt_path": "/mnt/data/gateway/test.prompt",
  "response_path": "/mnt/data/gateway/response.json",
  "llm_used": "ollama-mistral-7b",
  "timestamp": "2025-07-05T22:20:00",
  "summary": "Log analysis completed successfully.",
  "tags": ["jenkins", "logs", "ai"]
}
```

Stored as:

```
/mnt/data/mcp/mcp-20250705-2220-bf11c2b3-21c2-4c9b-81f2-e8077f80e937.json
```


## 👨‍💻 Author

- **Dani** – [@dorado-ai-devops](https://github.com/dorado-ai-devops)

## 🛡 License

GNU General Public License v3.0
