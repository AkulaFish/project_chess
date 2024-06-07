from http import HTTPStatus

from fastapi import FastAPI

from api import healthcheck_router, user_router

app = FastAPI()

app.include_router(healthcheck_router)
app.include_router(user_router)
