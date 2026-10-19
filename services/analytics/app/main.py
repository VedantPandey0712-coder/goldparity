from dataclasses import asdict

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings
from app.contracts import CONTRACTS

app = FastAPI(title="GoldParity Analytics")

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/contracts")
def list_contracts():
    return [asdict(spec) for spec in CONTRACTS.values()]
