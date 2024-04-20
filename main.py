from http import HTTPStatus

from fastapi import FastAPI

app = FastAPI()


@app.get("/health", status_code=HTTPStatus.OK)
def health_check():
    return {
        "status": "success",
    }
