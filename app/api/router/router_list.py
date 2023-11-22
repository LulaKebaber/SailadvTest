from fastapi import Depends, HTTPException, status

from ..services.db_service import Service, get_service
from . import router
from ..schemas import system_schemas, variable_schemas


@router.get("/list", status_code=status.HTTP_200_OK)
def get_system_list(
        svc: Service = Depends(get_service)
):
    systems = svc.system_repository.get_systems_with_variables()
    return systems



