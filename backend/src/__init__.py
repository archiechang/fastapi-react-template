from fastapi import FastAPI
from src.routers import items


def create_app():
    app = FastAPI()
    app.include_router(items.router)
    return app