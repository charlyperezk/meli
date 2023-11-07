from utils.config import Config
from utils.exceptions import VariableNotFound, ConfigError

class AuthConfig(Config):
    """Configuration for authentication-related variables.

    Attributes:
        CLIENT_ID (str): The client ID for authentication.
        CLIENT_SECRET (str): The client secret for authentication.
        REDIRECT_URI (str): The redirect URI for authentication.
        CODE (str): The authentication code.
    """

    CLIENT_ID: str = ""
    CLIENT_SECRET: str = ""
    REDIRECT_URI: str = ""
    CODE: str = ""

    def __init__(self) -> None:
        """Initializes an AuthConfig instance.

        Retrieves authentication variables or raises an error if not found.
        """
        try:
            self.CLIENT_ID = self.get_var("CLIENT_ID")
            self.CLIENT_SECRET = self.get_var("CLIENT_SECRET")
            self.REDIRECT_URI = self.get_var("REDIRECT_URI")
            self.CODE = self.get_var("CODE")
        except VariableNotFound as e:
            raise ConfigError(e)

    def get_data(self):
        pass

class ConnectionConfig(AuthConfig):
    """Configuration for connection-related data.

    Retrieves data for connecting to an external service.

    Inherits from AuthConfig for authentication variables.
    """

    def get_data(self) -> dict:
        """Get data for connection configuration.

        Returns:
            dict: Configuration data for connecting to an external service.
        """
        return {
            "grant_type": "authorization_code",
            "client_id": self.CLIENT_ID,
            "client_secret": self.CLIENT_SECRET,
            "code": self.CODE,
            "redirect_uri": self.REDIRECT_URI,
        }

class RefreshConfig(AuthConfig):
    """Configuration for refresh token.

    Retrieves data for refreshing the connection to an external service.

    Inherits from AuthConfig for authentication variables.
    """

    def get_data(self) -> dict:
        """Get data for refresh configuration.

        Returns:
            dict: Configuration data for refreshing the connection to an external service.
        """
        return {
            "grant_type": "refresh_token",
            "client_id": self.CLIENT_ID,
            "client_secret": self.CLIENT_SECRET,
            "redirect_uri": self.REDIRECT_URI
        }
