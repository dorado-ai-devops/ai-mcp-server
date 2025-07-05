from fastapi import FastAPI
from routes import register

app = FastAPI(title="ai-mcp-server")

app.include_router(register.router, prefix="/mcp", tags=["MCP"])
