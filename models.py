from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime
from uuid import uuid4

class MCPMessage(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()), description="UUID único del mensaje MCP")
    source: str = Field(..., description="Origen del mensaje (e.g., jenkins)")
    type: str = Field(..., description="Tipo de mensaje (e.g., pipeline-execution)")
    microservice: str = Field(..., description="Servicio IA involucrado")
    prompt_path: str
    response_path: str
    llm_used: str
    timestamp: datetime
    summary: Optional[str] = None
    tags: List[str] = Field(default=[])
