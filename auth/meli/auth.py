from auth.security import TokenEncryptor
from auth.meli.auth_status import MeliAuthStatus, ConnectionRequest, RefreshConnRequest
from database.client import DataBaseClient
from datetime import datetime
from utils.exceptions import AuthenticationError, DataBaseError, NotHandledError
import logging
import asyncio


class AuthClient(MeliAuthStatus, TokenEncryptor):
    """Handles authentication with Mercado Libre API.

    Attributes:
        db (DataBaseClient): Database client for data storage.
    """

    def __init__(self, db: DataBaseClient) -> None:
        """Initializes an AuthClient instance.

        Args:
            db (DataBaseClient): Database client for data storage.
        """
        self._db = db

    async def start_token_encryptor(self):
        """Starts the token encryption process asynchronously."""
        await self._setup_token()

    def _connection(self) -> dict:
        """Establishes a connection and handles authentication.

        Returns:
            dict: Authentication data.
        """
        try:
            asyncio.run(self.start_token_encryptor())
            logging.info("Searching credentials...")
            connection = self.credential(db=self._db)
            logging.info("Supervising status...")
            supervise = self.supervise(db=self._db)
        except DataBaseError as e:
            raise DataBaseError(e)
        except AuthenticationError as e:
            raise AuthenticationError(e)
        except Exception as e:
            raise NotHandledError(e)
        finally:
            try:
                logging.info("Supervised.")
                if connection and supervise:
                    logging.info("Valid credential found. Date: {}" .format(connection["date"]))
                    return self.decrypt(connection["access_token"])
                elif connection and not supervise:
                    logging.warning("Expired token. Date: {}" .format(connection["date"]))
                    data_req = RefreshConnRequest(refresh_token=self.decrypt(connection["refresh_token"]))
                    logging.info("Trying to refresh connection.")
                elif not connection:
                    logging.warning("No credential found.")
                    data_req = ConnectionRequest()
                    logging.info("Connecting.")
                new_connection = self.encrypt_connection_data(data_req.authenticate())
                if new_connection:
                    time = datetime.now()
                    logging.info("New valid connection created with date {}." .format(time))
                else:
                    logging.error("Connection failed.")
                    raise AuthenticationError("Connection failed.")
                self._db._save(object=new_connection)
                logging.info("Connection tested.")
                return self.decrypt(new_connection.access_token)
            except DataBaseError as e:
                raise DataBaseError(e)
            except AuthenticationError as e:
                raise AuthenticationError(e)
            except Exception as e:
                raise NotHandledError(e)
