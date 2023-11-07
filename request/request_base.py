from requests import Response
import requests

class Request:
    """HTTP request utility class for making API requests.

    This class provides methods to send GET and POST requests to a specified URL.
    It also allows for specifying headers, cookies, data, and parameters.

    Attributes:
        url (str): The URL to send the request to.
        headers (dict): HTTP headers to include in the request.
        cookies (dict): Cookies to include in the request.
        data (dict): Data to include in the request, used for POST requests.
        params (dict): URL parameters to include in the request.

    Methods:
        get() -> Response: Send a GET request and return the response object.
        post() -> Response: Send a POST request with JSON data and return the response object.
        to_dict() -> dict: Convert the request details to a dictionary.
    """

    def __init__(self, url: str, headers: dict = None, cookies: dict = None, data: dict = None, params: dict = None) -> None:
        """Initialize the Request object with request details.

        Args:
            url (str): The URL to send the request to.
            headers (dict): HTTP headers to include in the request.
            cookies (dict): Cookies to include in the request.
            data (dict): Data to include in the request, used for POST requests.
            params (dict): URL parameters to include in the request.
        """
        self.url = url
        self.headers = headers
        self.cookies = cookies
        self.data = data
        self.params = params

    def get(self) -> Response:
        """Send a GET request and return the response object.

        Returns:
            Response: The response object received from the GET request.
        """
        return requests.get(self.url, headers=self.headers, cookies=self.cookies, params=self.params)

    def post(self) -> Response:
        """Send a POST request with JSON data and return the response object.

        Returns:
            Response: The response object received from the POST request.
        """
        return requests.post(self.url, json=self.data, headers=self.headers, cookies=self.cookies)

    def to_dict(self) -> dict:
        """Convert the request details to a dictionary.

        Returns:
            dict: A dictionary containing the request details.
        """
        return {
            'url': self.url,
            'headers': self.headers,
            'data': self.data,
        }
