from cryptography.fernet import Fernet
from database.models.connection import Connection
from utils.config import Config
from utils.exceptions import ConfigError, VariableNotFound
import asyncio

class TokenEncryptor(Config):
    """Class for encrypting and decrypting tokens.

    This class manages token encryption and decryption operations.

    Attributes:
        key (str): The encryption key.
        fernet (Fernet): Fernet cipher for encryption and decryption.
    """

    key: str
    fernet: Fernet

    async def _setup_token(self) -> None:
        """Set up the encryption key and Fernet cipher.

        Initializes the encryption key and the Fernet cipher for future use.

        Returns:
            None
        """
        try:
            self.key = self.get_var("SECRET_KEY")
        except VariableNotFound as e:
            await self._set_secret_key()
        finally:
            try:
                self.fernet = Fernet(self.key)
            except ValueError:
                raise ConfigError("SECRET_KEY WITH INVALID FORMAT")

    def encrypt(self, token) -> str:
        """Encrypt a token.

        Args:
            token (str): The token to be encrypted.

        Returns:
            str: The encrypted token.
        """
        encrypted_token = self.fernet.encrypt(token.encode())
        return encrypted_token

    def encrypt_connection_data(self, connection: Connection) -> Connection:
        """Encrypt connection data.

        Encrypts the access and refresh tokens in a Connection object.

        Args:
            connection (Connection): The Connection object to encrypt.

        Returns:
            Connection: The Connection object with encrypted tokens.
        """
        connection.access_token = self.encrypt(connection.access_token)
        connection.refresh_token = self.encrypt(connection.refresh_token)
        return connection

    def decrypt(self, encrypted_token) -> str:
        """Decrypt an encrypted token.

        Args:
            encrypted_token: The token to be decrypted.

        Returns:
            str: The decrypted token.
        """
        decrypted_token = self.fernet.decrypt(encrypted_token).decode()
        return decrypted_token

    async def _set_secret_key(self) -> None:
        """Generate and append a new secret key.

        Generates a new secret key, appends it to the configuration, and sets it as the encryption key.

        Returns:
            None
        """
        key = Fernet.generate_key()
        encoded_key = key.decode()
        await self._append_encoded_key(encoded_key)
