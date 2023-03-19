"""Configuration module."""


from pydantic import BaseSettings


class DatabaseConfig(BaseSettings):
    """Database configuration.

    Attributes:
        dsn (str): A DSN-style database connection string.

    """

    dsn: str = "sqlite:///impact.db"

    class Config:
        """Pydantic settings object configuration."""

        env_prefix = "impact_db_"


class ApplicationConfig(BaseSettings):
    """Application configuration.

    Attributes:
        production (bool): Determines some behavior.

    """

    production: bool
    database: DatabaseConfig = DatabaseConfig()

    class Config:
        """Pydantic settings object configuration."""

        env_prefix = "impact_"
