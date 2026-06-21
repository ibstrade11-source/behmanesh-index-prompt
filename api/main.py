from fastapi import FastAPI
from api.routes.bsi import router as bsi_router
from api.mcp import mcp_router

app = FastAPI(title="BSI Auto System v1.0")
app.include_router(bsi_router, prefix="/bsi")
app.include_router(mcp_router)

@app.get("/health")
async def health():
    return {"status": "BSI Engine is running!", "version": "3.4.1"}
