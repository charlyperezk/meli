from __future__ import annotations
from abc import ABC, abstractmethod

class UserControl(ABC):
    """Abstract base class for user control in a MercadoLibre request system.

    This class defines two abstract methods that must be implemented by subclasses:
    - user_request(): Handles the user's request to the system.
    - generate_query(): Generates a query for the MercadoLibre API request.

    Subclasses must provide implementations for these methods.

    Attributes:
        None

    Methods:
        @abstractmethod user_request(self): Handles the user's request to the system.
        @abstractmethod generate_query(self): Generates a query for the MercadoLibre API request.
    """
    
    @abstractmethod
    def user_request(self):
        """Handles the user's request to the system.

        Subclasses must implement this method to process the user's input and initiate an API request.
        """
        pass
    
    @abstractmethod
    def generate_query(self):
        """Generates a query for the MercadoLibre API request.

        Subclasses must implement this method to create a query based on user input and settings.
        """
        pass
