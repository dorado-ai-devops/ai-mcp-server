import os
import json
from models import MCPMessage
from datetime import datetime

SAVE_DIR = "/mnt/data/mcp/"

def write_mcp_message(msg: MCPMessage):
    os.makedirs(SAVE_DIR, exist_ok=True)
    timestamp_str = msg.timestamp.strftime("%Y%m%d-%H%M%S")
    filename = f"mcp-{timestamp_str}-{msg.id}.json"
    path = os.path.join(SAVE_DIR, filename)

    with open(path, "w", encoding="utf-8") as f:
        json.dump(msg.model_dump(mode="json"), f, ensure_ascii=False, indent=2)