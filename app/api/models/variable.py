from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from ...database import Base


class Variable(Base):
    __tablename__ = "variable"

    id = Column(Integer, primary_key=True, index=True)
    system_id = Column(Integer, ForeignKey("system.id"))
    name = Column(String, index=True)
    type = Column(String)

    system = relationship("System", back_populates="variables")
