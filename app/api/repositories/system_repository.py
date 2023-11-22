from sqlalchemy.orm import Session
from typing import Optional, List, Any
from ..models.system import System, Variable


class SystemRepository:
    def __init__(self, database: Session):
        self.database = database

    def get_all_systems(self) -> list[Any]:
        systems = self.database.query(System).all()
        if not systems:
            return []

        return [{'name': system.name, 'id': str(system.id)} for system in systems]

    def get_system_by_id(self, system_id: str) -> Optional[dict[str, str]]:
        system = self.database.query(System).filter(System.id == system_id).first()
        if not system:
            return {}

        return {'id': str(system.id), 'name': system.name}

    def add_new_system(self, system_name: str) -> Optional[dict[str, str]]:
        system = System(name=system_name)
        self.database.add(system)
        self.database.commit()
        self.database.refresh(system)

        return {"id": str(system.id), "name": system.name}

    def delete_system_by_id(self, system_id: str) -> dict[str, str]:
        deleted_system = self.database.query(System).filter(System.id == system_id).delete()
        if not deleted_system:
            return {}
        self.database.commit()

        return {"message": f"System with id {system_id} was deleted"}

    def update_system_by_id(self, system_id: str, system_name: str) -> dict[str, str]:
        updated_system = self.database.query(System).filter(System.id == system_id).update(
            {'name': system_name}
        )
        if not updated_system:
            return {}
        self.database.commit()

        return {"id": str(system_id), "name": system_name}

    def get_systems_with_variables(self) -> List[Any]:
        systems = self.database.query(System).all()
        variables = self.database.query(Variable).all()
        systems_with_variables = []
        for system in systems:
            systems_with_variables.append({
                'id': str(system.id),
                'system': f'system {system.id}',
                'variables': [
                    {
                        'id': str(variable.id),
                        'system_id': str(variable.system_id),
                        'name': variable.name,
                        'type': variable.type,
                    } for variable in variables if variable.system_id == system.id
                ]
            })

        return systems_with_variables

