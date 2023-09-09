from fastapi import FastAPI, APIRouter
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from pathlib import Path

from src.routers.ml_models import models_router

FRONTEND_DIR = Path(__file__).parent.resolve().parents[1] / "frontend"

app = FastAPI(version="1.0.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # FIXME: This is not secure. Required for dev frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.mount("/static", StaticFiles(directory=FRONTEND_DIR, html=True), name='static')

v1_router = APIRouter()
v1_router.include_router(models_router, prefix="/models", tags=["models"])
app.include_router(v1_router, prefix="/v1")
