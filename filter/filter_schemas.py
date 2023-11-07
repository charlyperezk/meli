class FilterBase:
    """Base class representing a filter for querying MercadoLibre products.

    Attributes:
        id (str): Unique identifier for the filter.
        name (str): Name or label of the filter.
        code (str): Internal code associated with the filter.
        category (str): Category to which the filter belongs (optional).
        options (list): List of available options for the filter (optional).
        selected (bool): Indicates if the filter is selected (optional).

    Methods:
        to_dict(): Converts the filter attributes to a dictionary.
    """

    def __init__(self, id: str, name: str, code: str, category: str = None, options: list = None, selected: bool = False) -> None:
        """Initialize a FilterBase object.

        Args:
            id (str): Unique identifier for the filter.
            name (str): Name or label of the filter.
            code (str): Internal code associated with the filter.
            category (str, optional): Category to which the filter belongs.
            options (list, optional): List of available options for the filter.
            selected (bool, optional): Indicates if the filter is selected.
        """

        self.id = id
        self.name = name
        self.code = code
        self.category = category
        self.options = options
        self.selected = selected

    def to_dict(self) -> dict:
        """Convert the filter attributes to a dictionary.

        Returns:
            dict: Dictionary containing filter attributes.
        """

        return {
            'id': self.id,
            'name': self.name,
            'code': self.code,
            'category': self.category,
            'selected': self.selected
        }

    def __str__(self):
        return f"{self.__class__.__name__}({self.to_dict()})"


class FilterOptionBase:
    """Base class representing an option for a filter in MercadoLibre product queries.

    Attributes:
        id (str): Unique identifier for the option.
        name (str): Name or label of the option.
        code (str): Internal code associated with the option.
        category (str): Category to which the option belongs (optional).
        selected (bool): Indicates if the option is selected (optional).

    Methods:
        to_dict(): Converts the option attributes to a dictionary.
    """

    def __init__(self, id: str, name: str, code: str, category: str = None, selected: bool = False) -> None:
        """Initialize a FilterOptionBase object.

        Args:
            id (str): Unique identifier for the option.
            name (str): Name or label of the option.
            code (str): Internal code associated with the option.
            category (str, optional): Category to which the option belongs.
            selected (bool, optional): Indicates if the option is selected.
        """

        self.id = id
        self.name = name
        self.code = code
        self.category = category
        self.selected = selected

    def to_dict(self) -> dict:
        """Convert the option attributes to a dictionary.

        Returns:
            dict: Dictionary containing option attributes.
        """

        return {
            'id': self.id,
            'name': self.name,
            'code': self.code,
            'category': self.category,
            'selected': self.selected
        }
