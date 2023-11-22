from sqlalchemy.orm import Session
from ..models.variable import Variable


class VariableRepository:
    def __init__(self, database: Session):
        self.database = database

    def get_all_variables(self):
        variables = self.database.query(Variable).all()
        if not variables:
            return []

        return [{
            'id': str(variable.id),
            'system_id': str(variable.system_id),
            'name': variable.name,
            'type': variable.type,
        } for variable in variables]

    def get_variable_by_id(self, variable_id: str):
        variable = self.database.query(Variable).filter(Variable.id == variable_id).first()
        if not variable:
            return {}

        return {
            'id': str(variable.id),
            'system_id': str(variable.system_id),
            'name': variable.name,
            'type': variable.type,
        }

    def add_new_variable(self, system_id: str, name: str, type: str):
        variable = Variable(system_id=system_id, name=name, type=type)
        self.database.add(variable)
        self.database.commit()
        self.database.refresh(variable)

        return {
            'id': str(variable.id),
            'system_id': str(variable.system_id),
            'name': variable.name,
            'type': variable.type,
        }

    def delete_variable_by_id(self, variable_id: str):
        self.database.query(Variable).filter(Variable.id == variable_id).delete()
        self.database.commit()

        return {"message": f"Variable with id {variable_id} was deleted"}

    def update_variable_by_id(self, variable_id: str, system_id: str, name: str, type: str):
        self.database.query(Variable).filter(Variable.id == variable_id).update(
            {'system_id': system_id, 'name': name, 'type': type}
        )
        self.database.commit()

        return {
            'id': str(variable_id),
            'system_id': str(system_id),
            'name': name,
            'type': type,
        }