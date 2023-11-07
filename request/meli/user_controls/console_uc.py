from filter.filter_selection import SelectionHandler
import json
from request.request_base import Request
from request.meli.request_settings import RequestSettings
from request.meli.request_user_control import UserControl
from utils.http_request import CategoryPredictor, CategoryAttributes
from utils.exceptions import SelectionError
from typing import List

class ConsoleUserControl(UserControl):
    """Console-based user control for MercadoLibre requests.

    This class provides a console-based interface for users to input requests for MercadoLibre data.
    It inherits from the abstract base class UserControl and implements its abstract methods.

    Attributes:
        sel_handler (SelectionHandler): An instance of SelectionHandler to manage filter selections.

    Methods:
        user_request(request_settings: RequestSettings): Handles user requests and interacts with the user.
        get_attrs(key, credential): Retrieves category attributes based on user input.
        generate_query(filters: List[dict]): Generates a query based on selected filters.
    """

    def __init__(self) -> None:
        """Initialize the ConsoleUserControl.

        Initializes an instance of SelectionHandler.

        Args:
            None
        """
        self.sel_handler: SelectionHandler

    def user_request(self, request_settings: RequestSettings):
        """Handle user requests and interact with the user.

        This method allows users to input requests and interact with the MercadoLibre system.
        It implements the user_request method from the UserControl abstract class.

        Args:
            request_settings (RequestSettings): The request settings object.

        Returns:
            Response or None: The API response or None if no response is available.
            str: The URL used for the request.
        """
        print("")
        while True:
            self.sel_handler = SelectionHandler()
            try:
                keyword = input("Enter your request (or 'q' to quit): ")
                if keyword == "q":
                    return None, None
                attrs = self.get_attrs(keyword, request_settings.credential)
                if attrs:
                    selection = self.sel_handler.choose(attrs)
                    if selection:
                        query = self.generate_query(attrs)
                        request_settings.url += query
                request_settings.url += "&q={}".format(keyword)
                request = Request(url=request_settings.url,
                                  headers=request_settings.credential)
                return request.get(), request_settings.url
            except Exception as e:
                raise SelectionError(e)

    def get_attrs(self, key, credential) -> json or None:
        """Retrieve category attributes based on user input.

        This method uses the CategoryPredictor and CategoryAttributes classes to predict categories
        and retrieve their attributes based on user input.

        Args:
            key (str): The user's input keyword.
            credential (dict): The API credentials.

        Returns:
            json or None: The retrieved category attributes or None if no attributes are available.
        """
        category_predictor = CategoryPredictor(key, credential)
        try:
            category = category_predictor.get()
            category_name = category.json()[0].get("domain_name", "")
            category_id = category.json()[0].get("category_id", "")
            print("Category predict {}" .format(category_name))
            category_attr = CategoryAttributes(category_id, credential)
            attrs = category_attr.get().json()
            return attrs
        except Exception:
            return None

    def generate_query(self, filters: List[dict]) -> str:
        """Generate a query based on selected filters.

        This method generates a query for the MercadoLibre API request based on selected filters.

        Args:
            filters (List[dict]): The selected filters.

        Returns:
            str: The generated query.
        """
        query = "?"
        for f in filters:
            selected_options = [fo for fo in f.get(
                'values', []) if fo.get('selected')]
            if selected_options:
                if query[-1] != "?":
                    query += "&"
                query += f"{f['id']}="
                query += ",".join(fo['id'] for fo in selected_options)
        return query
