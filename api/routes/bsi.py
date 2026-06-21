from fastapi import APIRouter
from core.bsi_engine import compute_bsi
from core.bsi_pipeline import run_pipeline
from datetime import datetime

router = APIRouter()

BSI_VERSION = "3.4.2"
ENGINE_VERSION = "bsi-core-1.0"


@router.get("/version")
def version():
    return {
        "bsi_version": BSI_VERSION,
        "engine": ENGINE_VERSION,
        "pipeline_stages": ["BSI", "EIG", "ECC", "DRAFT", "REIG", "FINAL"],
        "api_version": "1.2.0",
        "endpoints": ["/bsi/score", "/bsi/analyze", "/bsi/compare", "/bsi/version"]
    }


@router.post("/score")
def score(payload: dict):
    text = payload.get("text", "")
    detail = payload.get("detail", False)
    full_pipeline = payload.get("pipeline", False)

    if len(text) < 10:
        return {"error": {"code": "TEXT_TOO_SHORT", "message": "Minimum length is 10"}}

    result = compute_bsi(text)
    details = result.get("details", {})

    if full_pipeline:
        return run_pipeline(text, details)

    metrics = details.get("metrics", {})
    layers = details.get("bsi_layers", {})

    response = {
        "version": BSI_VERSION,
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


@router.post("/analyze")
def analyze(payload: dict):
    text = payload.get("text", "")
    if len(text) < 10:
        return {"error": {"code": "TEXT_TOO_SHORT", "message": "Minimum length is 10"}}
    result = compute_bsi(text)
    details = result.get("details", {})
    return run_pipeline(text, details)


@router.post("/compare")
def compare(payload: dict):
    text_a = payload.get("text_a", "")
    text_b = payload.get("text_b", "")

    if len(text_a) < 10 or len(text_b) < 10:
        return {"error": {"code": "TEXT_TOO_SHORT", "message": "Both texts must be at least 10 chars"}}

    result_a = compute_bsi(text_a)
    result_b = compute_bsi(text_b)

    bsi_a = result_a["bsi"]
    bsi_b = result_b["bsi"]
    eig_a = result_a["eig"]
    eig_b = result_b["eig"]

    if bsi_a > bsi_b:
        winner = "text_a"
        margin = round(bsi_a - bsi_b, 3)
    elif bsi_b > bsi_a:
        winner = "text_b"
        margin = round(bsi_b - bsi_a, 3)
    else:
        winner = "tie"
        margin = 0.0

    return {
        "version": BSI_VERSION,
        "timestamp": datetime.utcnow().isoformat(),
        "text_a": {
            "bsi_score": bsi_a,
            "eig_score": eig_a,
            "interpretation": result_a["label"]
        },
        "text_b": {
            "bsi_score": bsi_b,
            "eig_score": eig_b,
            "interpretation": result_b["label"]
        },
        "comparison": {
            "winner": winner,
            "bsi_margin": margin,
            "eig_delta": round(abs(eig_a - eig_b), 3),
            "verdict": (
                f"text_a از نظر BSI قوی‌تر است (+{margin})"
                if winner == "text_a" else
                f"text_b از نظر BSI قوی‌تر است (+{margin})"
                if winner == "text_b" else
                "هر دو متن امتیاز یکسانی دارند"
            )
        }
    }
