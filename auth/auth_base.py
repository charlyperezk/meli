from __future__ import annotations
from abc import ABC, abstractmethod

class Authentication(ABC):
    """Abstract base class for authentication.

    Defines an abstract method to authenticate the user.

    Attributes:
        None
    """

    @abstractmethod
    def authenticate(self):
        """Authenticate the user.

        This method should be implemented by subclasses to handle authentication logic.

        Returns:
            None
        """
        pass

class AuthStatusBase(ABC):
    """Abstract base class for authentication status.

    Defines abstract methods to supervise and retrieve credentials.

    Attributes:
        None
    """

    @abstractmethod
    def supervise(self):
        """Supervise the authentication status.

        This method should be implemented by subclasses to monitor and supervise the authentication status.

        Returns:
            None
        """
        pass

    def credential(self):
        """Retrieve authentication credentials.

        This method can be implemented by subclasses to fetch user credentials.

        Returns:
            None
        """
        pass
