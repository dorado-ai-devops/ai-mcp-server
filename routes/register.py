from fastapi import APIRouter, HTTPException
from models import MCPMessage
from services.writer import write_mcp_message

router = APIRouter()

@router.post("/register")
def register_message(msg: MCPMessage):
    try:
        write_mcp_message(msg)
        return {"status": "ok", "message": "MCP registrado"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
