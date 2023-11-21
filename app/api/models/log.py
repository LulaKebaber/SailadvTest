from sqlalchemy import Column, ForeignKey, Integer, String, Float, Boolean, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from ...database import Base


# class Log(Base):
#     __tablename__ = "log"
#
#     id = Column(Integer, primary_key=True, index=True)
#     timestamp = Column(DateTime, default=datetime.utcnow)
#     ip_address = Column(String)
#     endpoint = Column(String)
#     http_method = Column(String)