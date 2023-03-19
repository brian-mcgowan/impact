"""Dependency injection module."""


from dependency_injector import containers, providers

from impact.database import Database
from impact.repositories.activity import ActivityRepository
from impact.services.activity import ActivityService


class ApplicationDI(containers.DeclarativeContainer):
    """Application dependency injection container."""

    wiring_config = containers.WiringConfiguration(
        modules=["impact.endpoints.activities"]
    )

    config = providers.Configuration()

    database = providers.Singleton(
        Database,
        connection_url=config.database.dsn,
        echo=not config.production,
    )

    activity_repository = providers.Factory(
        ActivityRepository,
        session_factory=database.provided.session,
    )

    activity_service = providers.Factory(
        ActivityService,
        activity_repository=activity_repository,
    )
