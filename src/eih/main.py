from fastapi import FastAPI

from eih.config import settings

app = FastAPI(
    title=settings.app_name,
    debug=settings.debug,
)


@app.get("/health")
async def health_check() -> dict[str, str]:
    """
    Returns the health status of the application.

    Returns:
        A dictionary containing the status and service name.
    """
    return {
        "status": "healthy",
        "service": settings.app_name,
    }