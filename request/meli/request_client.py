from database.client import DataBaseClient
from database.models.connection import Connection
from database.models.request import RequestModel
from requests import Response
from request.meli.user_controls.console_uc import ConsoleUserControl
from request.meli.request_settings import Credential, RequestSettings
from utils.http_request import validate

class RequestClient:
    """Handles MercadoLibre product search requests and manages the database.

    Attributes:
        _db (DataBaseClient): An instance of the database client used for data storage.

    Methods:
        search(access_token: str) -> Response or None: Initiates a product search request, manages database records, and returns the response.

    Args:
        db (DataBaseClient): An instance of the database client used for data storage.
    """

    def __init__(self, db: DataBaseClient) -> None:
        """Initializes a RequestClient instance.

        Args:
            db (DataBaseClient): An instance of the database client used for data storage.
        """
        self._db = db

    def search(self, access_token: str) -> Response or None:
        """Initiates a product search request and manages database records.

        Args:
            access_token (str): The access token used for authentication.

        Returns:
            Response or None: The response from the product search request or None if unsuccessful.
        """
        print("\nWelcome to Intelicom")
        credential = Credential(access_token)
        request_settings = RequestSettings(credential)
        _r_usercontrol = ConsoleUserControl()
        response, url = _r_usercontrol.user_request(request_settings)
        if not response and not url:
            return None
        connection = self._db._last(Connection)
        req_bd = RequestModel(url=url, session=connection.id,
                              status_code=response.status_code)
        self._db._save(req_bd)
        if validate(response):
            return response.json()
        return None
