from auth.meli.auth_config import ConnectionConfig, RefreshConfig
from auth.auth_base import Authentication, AuthStatusBase
from database.client import DataBaseClient
from database.models.connection import Connection
from datetime import datetime, timedelta
from utils.exceptions import AuthenticationError, DataBaseError
from utils.http_request import validate
from utils.time import _exceeded
import requests

class MeliAuthStatus(AuthStatusBase):
    """Handles Mercado Libre authentication status.

    Attributes:
        THRESHOLD (int): Time threshold for checking the status.
    """

    THRESHOLD: int = 6

    def supervise(self, db: DataBaseClient) -> bool | None:
        """Supervises the authentication status.

        Args:
            db (DataBaseClient): Database client for data storage.

        Returns:
            bool | None: True if authentication is valid, None otherwise.
        """
        try:
            _last = db._last(Connection)
            now = datetime.now()
            threshold = timedelta(hours=self.THRESHOLD)
            if not _exceeded(t1=_last.date, t2=now, threshold=threshold):
                return True
            return None
        except DataBaseError as e:
            raise DataBaseError(e)
        except Exception as e:
            raise AuthenticationError(e)

    def credential(auth: Authentication, db: DataBaseClient) -> dict:
        """Retrieves authentication credentials.

        Args:
            auth (Authentication): Authentication object.
            db (DataBaseClient): Database client for data storage.

        Returns:
            dict | None: Authentication credentials if available, None otherwise.
        """
        try:
            _all = db._get_all(object=Connection)
            if len(_all) > 0:
                _last = db._last(object=Connection)
                return {
                    "date": _last.date,
                    "access_token": _last.access_token,
                    "refresh_token": _last.refresh_token
                }
            return None
        except DataBaseError as e:
            raise DataBaseError(e)
        except Exception as e:
            raise AuthenticationError(e)

class MeliAuthentication(Authentication):
    """Handles Mercado Libre authentication.

    Attributes:
        url (str): URL for authentication.
        headers (dict): Request headers.
    """

    def authenticate(self) -> dict or None:
        """Performs authentication and retrieves credentials.

        Returns:
            dict | None: Authentication credentials if available, None otherwise.
        """
        try:
            req = requests.post(
                url=self.url, data=self.data, headers=self.headers)
            if validate(req):
                access_token = req.json().get("access_token", "")
                refresh_token = req.json().get("refresh_token", "")
                data = Connection(access_token=access_token,
                                  refresh_token=refresh_token)
                return data
            return None
        except Exception as e:
            raise AuthenticationError(e)

class MeliAuthRequest(MeliAuthentication):
    """Handles Mercado Libre authentication requests.

    Attributes:
        url (str): URL for authentication.
        headers (dict): Request headers.
    """

    url: str = "https://api.mercadolibre.com/oauth/token"
    headers: dict = {
        "accept": "application/json",
        "content-type": "application/x-www-form-urlencoded"
    }

class ConnectionRequest(MeliAuthRequest):
    """Handles connection requests for authentication.

    Attributes:
        config (ConnectionConfig): Configuration for connection.
        data (dict): Request data.
    """

    config: ConnectionConfig = ConnectionConfig()
    data: dict = config.get_data()

class RefreshConnRequest(MeliAuthRequest):
    """Handles refresh connection requests for authentication.

    Attributes:
        config (RefreshConfig): Configuration for refresh connection.
        data (dict): Request data.
    """

    config: RefreshConfig = RefreshConfig()
    data: dict = config.get_data()

    def __init__(self, refresh_token: str) -> None:
        """Initializes a RefreshConnRequest.

        Args:
            refresh_token (str): Refresh token for authentication.
        """
        self.data["refresh_token"] = refresh_token
