from sqlalchemy import func
from sqlalchemy.orm import Session
from sqlalchemy.orm.exc import NoResultFound
from utils.exceptions import DataBaseError
from filter.filter_schemas import FilterBase

class DataBaseClient:
    """Database client for managing database interactions.

    This class is responsible for interacting with the database, including saving, querying, and committing transactions.

    Attributes:
        session (Session): The SQLAlchemy session used for database operations.
    """

    def __init__(self, session: Session) -> None:
        """Initialize the DatabaseClient.

        Args:
            session (Session): The SQLAlchemy session to use for database operations.
        """
        self._session = session

    def _save(self, object) -> None:
        """Save an object to the database.

        Args:
            object: The object to be saved to the database.

        Raises:
            DataBaseError: If an error occurs during the database operation.
        """
        try:
            self._session.add(object)
            self._session.commit()
        except Exception as e:
            raise DataBaseError(e)

    def _last(self, object):
        """Retrieve the most recent object of a specific type from the database.

        Args:
            object: The type of object to retrieve.

        Returns:
            object: The most recent object of the specified type.

        Raises:
            DataBaseError: If an error occurs during the database operation.
        """
        try:
            data = self._session.query(object).order_by(object.id.desc()).first()
            self.session_commit()
            return data
        except Exception as e:
            raise DataBaseError(e)

    def _get_all(self, object):
        """Retrieve all objects of a specific type from the database.

        Args:
            object: The type of object to retrieve.

        Returns:
            list: A list of objects of the specified type.

        Raises:
            DataBaseError: If an error occurs during the database operation.
        """
        try:
            data = self._session.query(object).all()
            return data
        except Exception as e:
            raise DataBaseError(e)

    def _get_by_id(self, object, id):
        """Retrieve an object of a specific type by its ID from the database.

        Args:
            object: The type of object to retrieve.
            id: The ID of the object to retrieve.

        Returns:
            object: The object with the specified ID, or None if not found.

        Raises:
            DataBaseError: If an error occurs during the database operation.
        """
        try:
            data = self._session.query(object).filter_by(id=id).one()
            return data
        except NoResultFound:
            return None
        except Exception as e:
            raise DataBaseError(e)

    def _get_filter_by_code(self, filter: FilterBase, category):
        """Retrieve a filter by its code and category.

        Args:
            filter (FilterBase): The filter schema to retrieve.
            category: The category to filter by.

        Returns:
            FilterBase: The filter matching the specified code and category, or None if not found.

        Raises:
            DataBaseError: If an error occurs during the database operation.
        """
        try:
            data = self._session.query(filter).filter_by(category=category).one()
            return data
        except NoResultFound:
            return None
        except Exception as e:
            raise DataBaseError(e)

    def session_commit(self) -> None:
        """Commit the current database session.

        This method commits the current database session, finalizing any pending database changes.

        Returns:
            None
        """
        self._session.commit()
