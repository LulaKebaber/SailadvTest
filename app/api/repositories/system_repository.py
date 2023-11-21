from sqlalchemy.orm import Session
from typing import Optional, List, Any
from ..models.system import System


class SystemRepository:
    def __init__(self, database: Session):
        self.database = database

    def get_all_systems(self) -> list[Any]:
        systems = self.database.query(System).all()
        if not systems:
            return []

        return [{'name': system.name, 'id': str(system.id)} for system in systems]

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