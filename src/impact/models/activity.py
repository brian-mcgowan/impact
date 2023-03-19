"""Activity-related data models."""


from typing import Optional

from pydantic import BaseModel
from sqlalchemy import Column, String

from impact.models.base import GlobalBaseModel, GlobalBaseORM


class Activity(GlobalBaseModel):
    """Activity data model.

    Attributes:
        title (str): A title for user reference.

    """

    title: str

    class Config:
        """Pydantic model configuration."""

        orm_mode = True


class ActivityCreateDTO(BaseModel):
    """Activity creation DTO.

    Attributes:
        title (str): A title for user reference.

    """

    title: str


class ActivityUpdateDTO(BaseModel):
    """Activity update DTO.

    Attributes:
        title (str): A title for user reference.

    """

    title: Optional[str]


class ActivityORM(GlobalBaseORM):
    """Activity persistence model.

    Attributes:
        title (str): A title for user reference.

    """

    __tablename__ = "activity"

    title = Column(String, nullable=False)
