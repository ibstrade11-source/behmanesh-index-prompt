from fastapi import APIRouter
from core.bsi_engine import compute_bsi

router = APIRouter()

@router.post("/score")
def score(payload: dict):
    result = compute_bsi(payload["text"])

    return {
        "bsi_score": result["bsi"],
        "eig_score": result["eig"],
        "interpretation": result["label"]
    }
