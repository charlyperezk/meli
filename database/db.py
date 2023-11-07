import os

from dotenv import load_dotenv
load_dotenv()

from utils.exceptions import DataBaseError

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

try:
    engine = create_engine(os.getenv("DATABASE_URL"))
except:
    raise DataBaseError("Failed creating engine")
Base = declarative_base()
