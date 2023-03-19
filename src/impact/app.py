"""Application factory module."""


from fastapi import FastAPI

from impact.config import ApplicationConfig
from impact.containers import ApplicationDI
from impact.endpoints import activities
from impact.utils import ping


def main() -> FastAPI:
    """Application factory function."""
    container = ApplicationDI()
    container.config.from_pydantic(ApplicationConfig())
    container.init_resources()

    if not container.config.get("production"):
        container.database().create_database()

    app = FastAPI()
    app.container = container

    app.include_router(activities.router)
    app.include_router(ping.router)

    return app
