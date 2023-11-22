from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime, timezone

from ...database import Base


class Log(Base):
    __tablename__ = "log"

    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
    ip_address = Column(String)
    endpoint = Column(String)
    http_method = Column(String)
