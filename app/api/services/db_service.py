from sqlalchemy.orm import Session
from fastapi import Depends

from ..repositories.system_repository import SystemRepository
from ..repositories.variable_repository import VariableRepository
from ..repositories.log_repository import LogRepository
from ...database import SessionDB


class Service:
    def __init__(self, db: Session):
        self.system_repository = SystemRepository(db)
        self.variable_repository = VariableRepository(db)
        self.log_repository = LogRepository(db)


def get_session() -> Session:
    db = SessionDB
    try:
        yield db
    finally:
        db.close()


def get_service(session: Session = Depends(get_session)):
    return Service(session)

