from fastapi import APIRouter
from core.bsi_engine import compute_bsi
from core.bsi_pipeline import run_pipeline
from datetime import datetime

router = APIRouter()

@router.post("/score")
def score(payload: dict):
    text = payload.get("text", "")
    detail = payload.get("detail", False)
    full_pipeline = payload.get("pipeline", False)

    if len(text) < 10:
        return {"error": {"code": "TEXT_TOO_SHORT", "message": "Minimum length is 10"}}

    result = compute_bsi(text)
    details = result.get("details", {})

    # حالت pipeline کامل
    if full_pipeline:
        return run_pipeline(text, details)

    metrics = details.get("metrics", {})
    layers = details.get("bsi_layers", {})

    response = {
        "version": "3.4.2",
        "timestamp": datetime.utcnow().isoformat(),
        "bsi_score": result["bsi"],
        "eig_score": result["eig"],
        "interpretation": result["label"]
    }

    if detail:
        response["components"] = metrics.get("BSI_criteria", {})
        response["eig_gaps"] = layers.get("meta", {}).get("EIG", {}).get("gaps", {})
        response["failure_modes"] = details.get("failure_modes", [])
        response["assumptions"] = layers.get("latent", {}).get("assumptions_excavated", [])
        response["themes"] = layers.get("latent", {}).get("themes", [])
        response["core_claim"] = layers.get("manifest", {}).get("core_claim", "")
        response["domain"] = details.get("domain", "")
        response["recommendations"] = [
            f for f in details.get("failure_modes", [])
            if f != "هیچ failure mode بحرانی شناسایی نشد"
        ]

    return response
