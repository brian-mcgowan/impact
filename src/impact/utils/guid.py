"""GUID module.

Enables going between database and Python uuid.UUID data type.
"""


import uuid

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.types import TypeDecorator, CHAR


class GUID(TypeDecorator):
    """Platform-independent GUID type.

    Uses PostgreSQL-native UUID type if available or CHAR(32) stringify hex
    representation if not available.
    """

    cache_ok = True

    impl = CHAR

    def load_dialect_impl(self, dialect):
        """Loads the appropriate type descriptor for the target database.

        Args:
            dialect: The database dialect.

        Returns:
            A type descriptor.

        """
        if dialect.name == "postgresql":
            return dialect.type_descriptor(UUID())
        else:
            return dialect.type_descriptor(CHAR(32))

    def process_bind_param(self, value, dialect):
        """Converts Python values in database types.

        Args:
            value: A Python value.
            dialect: The database dialect.

        Returns:
            A database-compatible value.

        """
        if value is None:
            return value
        elif dialect.name == "postgresql":
            return str(value)
        else:
            if not isinstance(value, uuid.UUID):
                return "%.32x" % uuid.UUID(value).int
            else:
                return "%.32x" % value.int

    def process_result_value(self, value, dialect):
        """Converts query results into Python types.

        Args:
            value: A value from the database.
            dialect: The database dialect.

        Returns:
            A Python value.

        """
        if value is None:
            return value
        else:
            if not isinstance(value, uuid.UUID):
                value = uuid.UUID(value)
            return value
