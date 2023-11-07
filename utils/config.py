import asyncio
from utils.exceptions import VariableNotFound
import os

class Config:
    """Configuration class to handle environment variables and secrets.

    This class provides methods for retrieving environment variables and
    appending an encoded secret key to a file.

    Methods:
        get_var(name: str) -> str: Retrieve the value of an environment variable.
        _append_encoded_key(encoded_key: str) -> None: Append an encoded secret key to a file.
    """

    @classmethod
    def get_var(self, name: str) -> str:
        """Retrieve the value of an environment variable.

        Args:
            name (str): The name of the environment variable to retrieve.

        Returns:
            str: The value of the environment variable.
        
        Raises:
            VariableNotFound: If the specified environment variable is not found.
        """
        v = os.getenv(name)
        if not v:
            raise VariableNotFound(f"Variable {name} not found.")
        return v

    async def _append_encoded_key(self, encoded_key: str) -> None:
        """Append an encoded secret key to a file.

        Args:
            encoded_key (str): The encoded secret key to append to the file.

        Writes the encoded secret key to a file named '.env'.
        """
        with open('.env', 'a') as file:
            file.write(f'SECRET_KEY="{encoded_key}"')
