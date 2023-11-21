from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from ...database import Base
from .variable import Variable

class System(Base):
    __tablename__ = "system"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    variables = relationship(Variable, back_populates="system", cascade="all, delete-orphan")
