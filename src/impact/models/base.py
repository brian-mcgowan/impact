"""Base models."""


from datetime import datetime
from uuid import UUID, uuid4

from pydantic import BaseModel
from sqlalchemy import Column, DateTime
from sqlalchemy.sql.functions import func

from impact.database import Base
from impact.utils.guid import GUID


def generate_id() -> str:
    """Generates a UUID-style identifier.

    Returns:
        str: A UUID.

    """
    return str(uuid4())


class GlobalBaseModel(BaseModel):
    """Global data model base.

    Attributes:
        id (UUID): Object identifier.
        created_at (datetime): Timestamp of creation.
        updated_at (datetime): Timestamp of last update.

    """

    id: UUID
    created_at: datetime
    updated_at: datetime


class GlobalBaseORM(Base):
    """Global data persistence model base.

    Attributes:
        id (UUID): Object identifier.
        created_at (datetime): Timestamp of creation.
        updated_at (datetime): Timestamp of last update.

    """

    __abstract__ = True

    id = Column(GUID(), primary_key=True, default=generate_id)
    created_at = Column(DateTime, default=func.current_timestamp())
    updated_at = Column(
        DateTime, default=func.current_timestamp(), onupdate=func.current_timestamp()
    )
