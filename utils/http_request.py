from requests import Response
from request.request_base import Request

class CategoryPredictor(Request):
    """Category predictor request class for MercadoLibre API.

    This class sends a request to the MercadoLibre API for domain discovery.

    Args:
        key (str): The search key for domain discovery.
        credentials (dict): A dictionary of request headers.

    Attributes:
        url (str): The URL for domain discovery.
        headers (dict): Request headers.
        cookies: None
        params: None
    """

    def __init__(self, key: str, credentials: dict) -> None:
        self.url = f"https://api.mercadolibre.com/sites/MLA/domain_discovery/search?q={key}"
        self.headers = credentials
        self.cookies = None
        self.params = None

class CategoryAttributes(Request):
    """Category attributes request class for MercadoLibre API.

    This class sends a request to the MercadoLibre API to retrieve category attributes.

    Args:
        category (str): The category ID for which to retrieve attributes.
        credentials (dict): A dictionary of request headers.

    Attributes:
        url (str): The URL for category attributes.
        headers (dict): Request headers.
        cookies: None
        params: None
    """

    def __init__(self, category: str, credentials: dict) -> None:
        self.url = f"https://api.mercadolibre.com/categories/{category}/attributes"
        self.headers = credentials
        self.cookies = None
        self.params = None

def validate(res: Response) -> bool:
    """Validate the response from the API.

    Args:
        res (Response): The response object.

    Returns:
        bool: True if the response status code is 200, indicating success; otherwise, False.
    """
    if res.status_code == 200:
        return True
    return False
