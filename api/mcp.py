from fastapi import APIRouter
from core.bsi_engine import compute_bsi
from datetime import datetime

mcp_router = APIRouter()

@mcp_router.get("/mcp")
def mcp_manifest():
    return {
        "schema_version": "v1",
        "name": "BSI Analyzer",
        "description": "Behmanesh Index — Epistemic evaluation framework v3.4.1",
        "tools": [
            {
                "name": "analyze_with_bsi",
                "description": "Evaluate intellectual content using BSI v3.4.1. Returns BSI score, EIG score, and interpretation.",
                "input_schema": {
                    "type": "object",
                    "properties": {
                        "text": {
                            "type": "string",
                            "description": "The text to evaluate"
                        },
                        "detail": {
                            "type": "boolean",
                            "description": "If true, returns full breakdown including components, gaps, and assumptions",
                            "default": False
                        }
                    },
                    "required": ["text"]
                }
            }
        ]
    }

@mcp_router.post("/mcp/call")
def mcp_call(payload: dict):
    tool = payload.get("tool")
    params = payload.get("params", {})

    if tool != "analyze_with_bsi":
        return {"error": {"code": "UNKNOWN_TOOL", "message": f"Tool '{tool}' not found"}}

    text = params.get("text", "")
    detail = params.get("detail", False)

    if len(text) < 10:
        return {"error": {"code": "TEXT_TOO_SHORT", "message": "Minimum length is 10"}}

    result = compute_bsi(text)
    details = result.get("details", {})
    metrics = details.get("metrics", {})
    layers = details.get("bsi_layers", {})

    response = {
        "version": "3.4.1",
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
        response["core_claim"] = layers.get("manifest", {}).get("core_claim", "")
        response["domain"] = details.get("domain", "")

    return {"result": response}
