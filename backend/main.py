import uvicorn

from src.config import settings

if __name__ == "__main__":
    uvicorn.run(
        app="src.app:app",
        host=settings.APP_HOST,
        port=settings.APP_PORT,
        reload=True if settings.ENV != "production" else False,
        workers=1,
    )
