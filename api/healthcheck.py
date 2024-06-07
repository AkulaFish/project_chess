from fastapi import APIRouter, status

healthcheck_router = APIRouter(tags=["Healthcheck"])


@healthcheck_router.get("/health", status_code=status.HTTP_200_OK)
def health_check():
    return {
        "status": "success",
    }
