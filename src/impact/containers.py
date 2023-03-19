"""Dependency injection module."""


from dependency_injector import containers, providers


class ApplicationDI(containers.DeclarativeContainer):
    """Application dependency injection container."""

    config = providers.Configuration()
