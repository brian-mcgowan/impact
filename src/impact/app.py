"""Application factory module."""


from fastapi import FastAPI

from impact.config import ApplicationConfig
from impact.containers import ApplicationDI
from impact.utils import ping


def main() -> FastAPI:
    """Application factory function."""
    container = ApplicationDI()
    container.config.from_pydantic(ApplicationConfig())
    container.init_resources()

    app = FastAPI()
    app.container = container

    app.include_router(ping.router)

    return app
