"""Activity service module."""


from typing import List
from uuid import UUID

from impact.models.activity import Activity, ActivityCreateDTO, ActivityUpdateDTO
from impact.repositories.activity import ActivityRepository


class ActivityService:
    """Handles business logic for `Activity` objects."""

    def __init__(self, activity_repository: ActivityRepository) -> None:
        """Constructor for `ActivityService`.

        Args:
            activity_repository (ActivityRepository): A repository for persisting
                `Activity` objects.

        """
        self._repository = activity_repository

    def create(self, activity: ActivityCreateDTO) -> Activity:
        """Creates an `Activity` object.

        Args:
            activity (ActivityCreateDTO): A DTO for creating `Activity` objects.

        Returns:
            Activity: An `Activity` object.

        """
        return self._repository.create(activity)

    def delete_by_id(self, activity_id: UUID) -> None:
        """Deletes an `Activity` object.

        Args:
            activity_id (UUID): A UUID identifying an `Activity` object.

        """
        self._repository.delete_by_id(activity_id)

    def get_by_id(self, activity_id: UUID) -> Activity:
        """Retrieves an `Activity` object.

        Args:
            activity_id (UUID): A UUID identifying an `Activity` object.

        Returns:
            Activity: An `Activity` object.

        """
        return self._repository.get_by_id(activity_id)

    def get_list(self) -> List[Activity]:
        """Retrieves a list of `Activity` objects.

        Returns:
            List[Activity]: A list of `Activity` objects.

        """
        return self._repository.get_list()

    def replace_by_id(self, activity_id: UUID, activity: ActivityCreateDTO) -> Activity:
        """Replaces an `Activity` object.

        Args:
            activity_id (UUID): A UUID identifying an `Activity` object.
            activity (ActivityUpdateDTO): A DTO for updating `Activity` objects.

        Returns:
            Activity: An `Activity` object.

        """
        return self._repository.replace_by_id(activity_id, activity)

    def update_by_id(self, activity_id: UUID, activity: ActivityUpdateDTO) -> Activity:
        """Partially updates an `Activity` object.

        Args:
            activity_id (UUID): A UUID identifying an `Activity` object.
            activity (ActivityUpdateDTO): A DTO for updating `Activity` objects.

        Returns:
            Activity: An `Activity` object.

        """
        return self._repository.update_by_id(activity_id, activity)
