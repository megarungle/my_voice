from fastapi import FastAPI, APIRouter
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware

from src.routers.ml_models import models_router

app = FastAPI(version="1.0.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # FIXME: This is not secure. Required for dev frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", include_in_schema=False)
def __redirect_to_docs():
    return RedirectResponse(url="/docs")


v1_router = APIRouter()
v1_router.include_router(models_router, prefix="/models", tags=["models"])
app.include_router(v1_router, prefix="/v1")
