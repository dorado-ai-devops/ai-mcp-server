# 🧠 ai-mcp-server

> Microservicio FastAPI para registrar y almacenar mensajes estructurados MCP (Mensajes de Contexto de Pipeline), conectando Jenkins, IA y dashboards en un sistema reflexivo.

Desarrollado en Python + FastAPI, 100% local y desplegado vía Helm + ArgoCD.

---

## 🚀 Características

- ✅ Registra mensajes MCP (origen, tipo, timestamp, microservicio, prompt, respuesta IA, etc.)
- 🧠 Cada mensaje incluye un `UUID` único + trazabilidad completa
- 🗂️ Guarda automáticamente en JSON (`/mnt/data/mcp/`) con nombres versionados
- 📁 Compatible con dashboards Streamlit y visualización CI
- 🧩 API REST tipo POST con validación Pydantic
- 🐳 Dockerizado y desplegable en Kubernetes (Kind + ArgoCD)

---

## 📦 Estructura del Proyecto

```
ai-mcp-server/
├── main.py                # Entrada FastAPI y router
├── models.py              # Esquemas MCPMessage (Pydantic)
├── routes/
│   └── register.py        # Endpoint principal POST /mcp/register
├── services/
│   └── writer.py          # Lógica para guardar mensajes MCP en JSON
├── requirements.txt       # Dependencias Python
├── Dockerfile             # Imagen contenedor
├── Makefile               # Build y despliegue automatizado
└── README.md              # Documentación del proyecto
```

---

## 🧩 Componentes

### `routes/register.py`

Define el endpoint REST principal:

```
POST /mcp/register
```

- Entrada esperada: JSON con campos `source`, `type`, `microservice`, `timestamp`, `prompt_path`, etc.
- Valida el mensaje con Pydantic y lo guarda en disco (`/mnt/data/mcp/`)

---

## 🧠 Lógica Interna

### `models.py`

Define el modelo MCPMessage:

- Campos: `id`, `source`, `type`, `timestamp`, `tags`, `summary`, etc.
- El `id` se genera automáticamente como UUID (`uuid4`)

### `writer.py`

- Construye nombre de archivo único con `timestamp + UUID`
- Guarda el mensaje como JSON legible (UTF-8, indentado)
- Estructura 100% compatible con posteriores indexadores (SQLite) o dashboards

---

## 🔁 Integración Jenkins

Desde cualquier pipeline de Jenkins puedes hacer un `curl` como:

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
    "summary": "Análisis automático completado sin errores.",
    "tags": ["jenkins", "logs", "ai"]
}'
```

---

## 🛠️ Primeros pasos (Local)

```bash
git clone git@github.com:dorado-ai-devops/ai-mcp-server.git
cd ai-mcp-server
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Ejecutar localmente

```bash
uvicorn main:app --reload --port 8001
```

---

## 💾 Ejemplo de archivo guardado

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
  "summary": "Análisis automático de logs completado sin errores.",
  "tags": ["jenkins", "logs", "ai"]
}
```

Guardado como:

```
/mnt/data/mcp/mcp-20250705-2220-bf11c2b3-21c2-4c9b-81f2-e8077f80e937.json
```


---

## 👨‍💻 Autor

- **Dani** – [@dorado-ai-devops](https://github.com/dorado-ai-devops)

---

## 🛡 Licencia

Licencia Pública General GNU v3.0
