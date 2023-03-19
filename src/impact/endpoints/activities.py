"""Activities endpoints.

Serves as the publicly addressable interface for interacting with `Activity` objects.
"""


from typing import List, Optional, Union
from uuid import UUID

from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends, Response, status

from impact.containers import ApplicationDI
from impact.models.activity import Activity, ActivityCreateDTO, ActivityUpdateDTO
from impact.services.activity import ActivityService
from impact.utils.errors import NotFoundError


router = APIRouter(prefix="/activities")


@router.post("/", response_model=Activity, status_code=status.HTTP_201_CREATED)
@inject
def create_activity(
    activity: ActivityCreateDTO,
    activity_service: ActivityService = Depends(
        Provide[ApplicationDI.activity_service]
    ),
) -> Activity:
    """Creates an `Activity` object and returns it to the client.

    Args:
        activity (ActivityCreateDTO): A DTO for creating `Activity` objects.
        activity_service (ActivityService): Application service for handling `Activity`
            operations.

    Returns:
        Activity: An `Activity` object.

    """
    return activity_service.create(activity)


@router.delete(
    "/{activity_id}", response_model=None, status_code=status.HTTP_204_NO_CONTENT
)
@inject
def delete_activity_by_id(
    activity_id: UUID,
    activity_service: ActivityService = Depends(
        Provide[ApplicationDI.activity_service]
    ),
) -> Optional[Response]:
    """Deletes an `Activity` object.

    Args:
        activity_id (UUID): A UUID identifying an `Activity` object.
        activity_service (ActivityService): Application service for handling `Activity`
            operations.

    """
    try:
        activity_service.delete_by_id(activity_id)
    except NotFoundError:
        return Response(status_code=status.HTTP_404_NOT_FOUND)
    # TODO: Check if explicit 204 response is needed here.


@router.get("/{activity_id}", response_model=Activity, status_code=status.HTTP_200_OK)
@inject
def get_activity_by_id(
    activity_id: UUID,
    activity_service: ActivityService = Depends(
        Provide[ApplicationDI.activity_service]
    ),
) -> Union[Activity, Response]:
    """Retrieves an `Activity` object and returns it to the client.

    Args:
        activity_id (UUID): A UUID identifying an `Activity` object.
        activity_service (ActivityService): Application service for handling `Activity`
            operations.

    Returns:
        Activity: An `Activity` object.

    """
    try:
        return activity_service.get_by_id(activity_id)
    except NotFoundError:
        return Response(status_code=status.HTTP_404_NOT_FOUND)


@router.get("/", response_model=List[Activity], status_code=status.HTTP_200_OK)
@inject
def get_activity_list(
    activity_service: ActivityService = Depends(
        Provide[ApplicationDI.activity_service]
    ),
) -> List[Activity]:
    """Retrieves a list of `Activity` objects and returns it to the client.

    Returns:
        List[Activity]: A list of `Activity` objects.
        activity_service (ActivityService): Application service for handling `Activity`
            operations.

    """
    return activity_service.get_list()


@router.put("/{activity_id}", response_model=Activity, status_code=status.HTTP_200_OK)
@inject
def replace_activity_by_id(
    activity_id: UUID,
    activity: ActivityCreateDTO,
    activity_service: ActivityService = Depends(
        Provide[ApplicationDI.activity_service]
    ),
) -> Union[Activity, Response]:
    """Replaces an `Activity` object and returns the new version to the client.

    Args:
        activity_id (UUID): A UUID identifying an `Activity` object.
        activity (ActivityUpdateDTO): A DTO for updating `Activity` objects.
        activity_service (ActivityService): Application service for handling `Activity`
            operations.

    Returns:
        Activity: An `Activity` object.

    """
    try:
        return activity_service.replace_by_id(activity_id, activity)
    except NotFoundError:
        return Response(status_code=status.HTTP_404_NOT_FOUND)


@router.patch("/{activity_id}", response_model=Activity, status_code=status.HTTP_200_OK)
@inject
def update_activity_by_id(
    activity_id: UUID,
    activity: ActivityUpdateDTO,
    activity_service: ActivityService = Depends(
        Provide[ApplicationDI.activity_service]
    ),
) -> Union[Activity, Response]:
    """Partially updates an `Activity` object and returns the new version to the client.

    Args:
        activity_id (UUID): A UUID identifying an `Activity` object.
        activity (ActivityUpdateDTO): A DTO for updating `Activity` objects.
        activity_service (ActivityService): Application service for handling `Activity`
            operations.

    Returns:
        Activity: An `Activity` object.

    """
    try:
        return activity_service.update_by_id(activity_id, activity)
    except NotFoundError:
        return Response(status_code=status.HTTP_404_NOT_FOUND)
