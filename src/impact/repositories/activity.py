"""Activity repository module."""


from contextlib import AbstractContextManager
from typing import Callable, List, Type
from uuid import UUID

from sqlalchemy.orm import Session

from impact.models.activity import (
    Activity,
    ActivityCreateDTO,
    ActivityORM,
    ActivityUpdateDTO,
)
from impact.utils.errors import NotFoundError


class ActivityNotFoundError(NotFoundError):
    """Emitted when an Activity cannot be found."""

    entity_name = "Activity"


class ActivityRepository:
    """Handles Activity persistence operations."""

    def __init__(
        self, session_factory: Callable[..., AbstractContextManager[Session]]
    ) -> None:
        """Constructor for `ActivityRepository`.

        Args:
            session_factory (Callable[..., AbstractContextManager[Session]]): The
                database session factory.

        """
        self.session_factory = session_factory

    @staticmethod
    def _create_activity(session: Session, activity: ActivityCreateDTO) -> ActivityORM:
        """Adds an `Activity` object to the database without committing.

        Args:
            session (Session): An active database session.
            activity (ActivityCreateDTO): A DTO for creating `Activity` objects.

        Returns:
            Activity: An `Activity` object.

        """
        activity = ActivityORM(**activity.dict())
        session.add(activity)
        return activity

    @staticmethod
    def _get_activity_by_id(
            session: Session, activity_id: UUID
    ) -> Type[ActivityORM]:
        """Retrieves an `ActivityORM` object from the database.

        Args:
            session (Session): An active database session.
            activity_id (UUID): A UUID identifying an `Activity` object.

        Returns:
            Activity: An `ActivityORM` object.

        """
        activity = (
            session.query(ActivityORM)
            .filter(ActivityORM.id == str(activity_id))
            .first()
        )
        if not activity:
            raise ActivityNotFoundError(activity_id)
        return activity

    def _delete_activity_by_id(self, session: Session, activity_id: UUID) -> None:
        """Removes an `Activity` object from the database without committing.

        Args:
            session (Session): An active database session.
            activity_id (UUID): A UUID identifying an `Activity` object.

        """
        activity = self._get_activity_by_id(session, activity_id)
        if not activity:
            raise ActivityNotFoundError(activity_id)
        session.delete(activity)

    def create(self, activity: ActivityCreateDTO) -> Activity:
        """Persists an `Activity` object to the database.

        Args:
            activity (ActivityCreateDTO): A DTO for creating `Activity` objects.

        Returns:
            Activity: An `Activity` object.

        """
        with self.session_factory() as session:
            activity = self._create_activity(session, activity)
            session.commit()
            session.refresh(activity)
            return Activity.from_orm(activity)

    def delete_by_id(self, activity_id: UUID) -> None:
        """Removes an `Activity` object from the database.

        Args:
            activity_id (UUID): A UUID identifying an `Activity` object.

        """
        with self.session_factory() as session:
            self._delete_activity_by_id(session, activity_id)
            session.commit()

    def get_by_id(self, activity_id: UUID) -> Activity:
        """Retrieves an `Activity` object from the database.

        Args:
            activity_id (UUID): A UUID identifying an `Activity` object.

        Returns:
            Activity: An `Activity` object.

        """
        with self.session_factory() as session:
            activity_orm = self._get_activity_by_id(session, activity_id)
            if not activity_orm:
                raise ActivityNotFoundError(activity_id)
            return Activity.from_orm(activity_orm)

    def get_list(self) -> List[Activity]:
        """Retrieves a list of `Activity` objects from the database.

        Returns:
            List[Activity]: A list of `Activity` objects.

        """
        with self.session_factory() as session:
            activity_orm_list = session.query(ActivityORM).all()
            return [
                Activity.from_orm(activity_orm) for activity_orm in activity_orm_list
            ]

    def replace_by_id(self, activity_id: UUID, activity: ActivityCreateDTO) -> Activity:
        """Replaces an `Activity` object in the database.

        Args:
            activity_id (UUID): A UUID identifying an `Activity` object.
            activity (ActivityUpdateDTO): A DTO for updating `Activity` objects.

        Returns:
            Activity: An `Activity` object.

        """
        with self.session_factory() as session:
            self._delete_activity_by_id(session, activity_id)
            activity = self._create_activity(session, activity)
            session.commit()
            session.refresh(activity)
            return Activity.from_orm(activity)

    def update_by_id(self, activity_id: UUID, activity: ActivityUpdateDTO) -> Activity:
        """Partially updates an `Activity` object in the database.

        Args:
            activity_id (UUID): A UUID identifying an `Activity` object.
            activity (ActivityUpdateDTO): A DTO for updating `Activity` objects.

        Returns:
            Activity: An `Activity` object.

        """
        with self.session_factory() as session:
            activity_orig = self._get_activity_by_id(session, activity_id)
            if not activity:
                raise ActivityNotFoundError(activity_id)
            for k, v in activity.dict().items():
                setattr(activity_orig, k, v)
            session.commit()
            session.refresh(activity_orig)
            return Activity.from_orm(activity_orig)
