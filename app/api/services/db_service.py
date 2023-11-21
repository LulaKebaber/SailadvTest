from sqlalchemy.orm import Session
from fastapi import Depends

from ..repositories.system_repository import SystemRepository
from ..repositories.variable_repository import VariableRepository
from ...database import SessionLocal


class Service:
    def __init__(self, db: Session):
        self.system_repository = SystemRepository(db)
        self.variable_repository = VariableRepository(db)


def get_session() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_service(session: Session = Depends(get_session)):
    return Service(session)

