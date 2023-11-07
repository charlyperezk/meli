from datetime import datetime

from sqlalchemy import Integer, Column, String, DateTime

from database.db import Base

class RequestModel(Base):
    __tablename__ = "request"

    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(DateTime(), default=datetime.now())    
    url = Column(String(200), nullable=True)
    session = Column(String(200), nullable=True)
    status_code = Column(Integer, nullable=True)