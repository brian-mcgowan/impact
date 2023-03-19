"""Database connection module."""


from contextlib import contextmanager, AbstractContextManager
from typing import Callable

from sqlalchemy import create_engine, orm
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session


Base = declarative_base()


class Database:
    """Database session factory."""

    def __init__(self, connection_url: str, echo: bool = False) -> None:
        """Database session factory.

        Args:
            connection_url (str): A DSN-style database connection string.
            echo (bool): Logs database commands if True. Defaults to False.

        """
        self._engine = create_engine(connection_url, echo=echo)
        self._session_factory = orm.scoped_session(
            orm.sessionmaker(
                autocommit=False,
                autoflush=False,
                bind=self._engine,
            )
        )

    def create_database(self) -> None:
        """Creates required database resources.

        Not intended for production use.
        """
        Base.metadata.create_all(self._engine)

    @contextmanager
    def session(self) -> Callable[..., AbstractContextManager[Session]]:
        """Session factory method.

        Rolls back the session on error.

        Yields:
            sqlalchemy.orm.Session: A SQLAlchemy session.

        """
        session: Session = self._session_factory()
        try:
            yield session
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()
