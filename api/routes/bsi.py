from fastapi import APIRouter
from core.bsi_engine import compute_bsi
from datetime import datetime

router = APIRouter()

@router.post("/score")
def score(payload: dict):
    text = payload.get("text", "")
    detail = payload.get("detail", False)

    if len(text) < 10:
        return {"error": {"code": "TEXT_TOO_SHORT", "message": "Minimum length is 10"}}

    result = compute_bsi(text)
    details = result.get("details", {})
    metrics = details.get("metrics", {})
    layers = details.get("bsi_layers", {})

    # خروجی پایه — همیشه
    response = {
        "version": "3.4.1",
        "timestamp": datetime.utcnow().isoformat(),
        "bsi_score": result["bsi"],
        "eig_score": result["eig"],
        "interpretation": result["label"]
    }

    # خروجی کامل — فقط با detail=true
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
