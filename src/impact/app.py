"""Application factory module."""


from fastapi import FastAPI

from impact.utils import ping


def main() -> FastAPI:
    """Application factory function."""
    app = FastAPI()

    app.include_router(ping.router)

    return app
