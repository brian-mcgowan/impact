"""Ping module.

Primarily used to check network connectivity.
"""


from fastapi import APIRouter, Response, status


router = APIRouter()


@router.get("/ping", status_code=status.HTTP_200_OK, include_in_schema=False)
def ping():
    """Returns an HTTP 200 OK response."""
    return Response(status_code=status.HTTP_200_OK)
