from sqlalchemy.orm import Session


class VariableRepository:
    def __init__(self, database: Session):
        self.database = database
