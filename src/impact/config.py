"""Configuration module."""


from pydantic import BaseSettings


class ApplicationConfig(BaseSettings):
    """Application configuration.

    Attributes:
        production (bool): Determines some behavior.

    """

    production: bool

    class Config:
        """Pydantic settings object configuration."""

        env_prefix = 'impact_'
