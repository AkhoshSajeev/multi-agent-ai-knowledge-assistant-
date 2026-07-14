from fastapi import FastAPI
from app.documents.router import router as document_router
from app.auth.router import router as auth_router
from app.db.database import Base, engine
from app.models.user import User


app = FastAPI(
    title="Multi-Agent AI Knowledge Assistant",
    version="1.0.0",
)

app.include_router(
    auth_router,
    prefix="/api/v1/auth",
    tags=["Authentication"],
)
app.include_router(
    document_router,
    prefix="/api/v1/documents",
    tags=["Documents"],
)

@app.get("/health")
def health():
    return {"status": "healthy"}

app.include_router(
    document_router,
    prefix="/api/v1/documents",
    tags=["Documents"],
)