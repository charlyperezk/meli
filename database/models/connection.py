from datetime import datetime

from sqlalchemy import Integer, Column, String, DateTime

from database.db import Base

class Connection(Base):
    __tablename__ = "connection"

    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(DateTime(), default=datetime.now())    
    access_token = Column(String(200), nullable=True)
    refresh_token = Column(String(200), nullable=True)