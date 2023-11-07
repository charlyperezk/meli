from database.db import engine, Base  # Importing the database engine and Base
from etl.etl_client import MeliClient  # Importing the ETL client
import logging, sys  # Importing the logging and sys modules
from sqlalchemy.orm import sessionmaker  # Importing the sessionmaker

# Loop through and remove existing log handlers
for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)

# Configure logging to display INFO-level log messages to the console
logging.basicConfig(stream=sys.stdout, level=logging.INFO)

# Create a new session using the sessionmaker and the database engine
session = sessionmaker(engine)()

# Initialize the MeliClient with the session and start the ETL process
meli = MeliClient(session=session)
meli.start()
