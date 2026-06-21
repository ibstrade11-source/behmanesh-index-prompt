from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict, List
from core.bsi_engine import BSIEngine

app = FastAPI(title="BSI Auto System v1.0")
engine = BSIEngine()

@app.post("/analyze")
async def analyze(request: Dict):
    return engine.run_batch(request)

@app.get("/health")
async def health():
    return {"status": "BSI Engine is running!"}
