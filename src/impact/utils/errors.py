"""Errors module.

Contains API-specific errors.
"""


from uuid import UUID


class NotFoundError(Exception):
    """Base class for fail-to-find type errors.

    Attributes:
        entity_name (str): The name of the entity.

    """

    entity_name: str

    def __init__(self, entity_id: UUID) -> None:
        """`NotFoundError` constructor.

        Args:
            entity_id (UUID): A UUID.
        """
        super().__init__(f"{self.entity_name} '{entity_id}' not found")
