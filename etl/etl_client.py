## TODO:
##  - Analysis
##  - Request density per session (Moderator)
##  - Load (Loader)
##  - Comments, docs, ...
##  - Logging / tests
##  - Execution time control (Timing)
##  - Error handling

from auth.meli.auth import AuthClient
from database.client import DataBaseClient
from etl.transform import Transformer
from request.meli.request_client import RequestClient
from sqlalchemy.orm import Session
import logging

class MeliClient:
    """Main class responsible for orchestrating the MercadoLibre client application.

    This class initializes the necessary components, including authentication, database access, data transformation, and request handling.

    Attributes:
        session (Session): SQLAlchemy session for database operations.
    """

    def __init__(self, session: Session) -> None:
        """Initialize the MeliClient.

        Args:
            session (Session): SQLAlchemy session for database operations.
        """
        self._db = DataBaseClient(session=session)
        self._auth = AuthClient(db=self._db)
        self.request_client = RequestClient(db=self._db)
        self.transformer = Transformer()

    def start(self):
        """Start the MercadoLibre client application.

        This method initiates the application, performs authentication, retrieves data using request client, and transforms the data.

        Returns:
            None
        """
        access_token = self._auth._connection()
        response = self.request_client.search(access_token)
        if response:
            self.transformer.transform(response)
        # self.loader.load(transformation)
