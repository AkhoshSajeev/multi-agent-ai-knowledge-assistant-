from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.auth.router import router as auth_router
from app.chat.router import router as chat_router
from app.documents.router import router as document_router

app = FastAPI(
    title="Multi-Agent AI Knowledge Assistant",
    version="1.0.0",
)

# Allow requests from the Next.js frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
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

app.include_router(
    chat_router,
    prefix="/api/v1/chat",
    tags=["Chat"],
)


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.get("/")
def test():
    return {"hello"}