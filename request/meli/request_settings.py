class Credential:
    """Represents user credentials with an access token.

    Attributes:
        access_token (str): The access token used for authentication.

    Methods:
        generate() -> dict: Generates a dictionary with an authorization header.

    Args:
        access_token (str): The access token used for authentication.
    """

    def __init__(self, access_token) -> None:
        """Initializes a Credential instance with an access token.

        Args:
            access_token (str): The access token used for authentication.
        """
        self.access_token = access_token

    def generate(self) -> dict:
        """Generates a dictionary with an authorization header.

        Returns:
            dict: A dictionary containing the authorization header with the access token.
        """
        return {
            'Authorization': f"Bearer {self.access_token}"
        }


class RequestSettings:
    """Represents settings for a request to the MercadoLibre API.

    Attributes:
        credential (dict): A dictionary with the authorization header.
        url (str): The URL for the API request.

    Methods:
        __init__(credential: Credential) -> None: Initializes a RequestSettings instance with a Credential.
    """

    def __init__(self, credential: Credential) -> None:
        """Initializes a RequestSettings instance with a Credential.

        Args:
            credential (Credential): An instance of the Credential class.
        """
        self.credential = credential.generate()
        self.url = "https://api.mercadolibre.com/sites/MLA/search"
