from fastapi import FastAPI
from http import HTTPStatus

app = FastAPI()


@app.get("/health", status_code=HTTPStatus.OK)
def health_check():
    return {
        "status": "success",
    }