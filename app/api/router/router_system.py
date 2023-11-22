from fastapi import Depends, HTTPException, status

from ..services.db_service import Service, get_service
from ..schemas import system_schemas, log_schemas
from . import router
from ..utils.validation import ValidationError


@router.get("/system", response_model=system_schemas.SystemListResponse, status_code=status.HTTP_200_OK)
def get_systems(
        svc: Service = Depends(get_service)
):
    systems = svc.system_repository.get_all_systems()
    ValidationError.entity_validation(systems, "No systems found")

    return {"systems": systems}


@router.post("/system", response_model=system_schemas.SystemCreateResponse, status_code=status.HTTP_201_CREATED)
def add_new_system(
        data: system_schemas.SystemCreateRequest,
        svc: Service = Depends(get_service),
):
    ValidationError.check_input_data(data.name)
    new_system = svc.system_repository.add_new_system(system_name=data.name)
    ValidationError.entity_validation(new_system, "Bad request")

    return new_system


@router.delete("/system/{system_id:str}", status_code=status.HTTP_200_OK)
def delete_system(
        system_id: str,
        svc: Service = Depends(get_service),
):
    deleted_system = svc.system_repository.delete_system_by_id(system_id=system_id)
    ValidationError.entity_validation(deleted_system, "System not found")

    return deleted_system


@router.put("/system/{system_id:str}", response_model=system_schemas.SystemUpdateResponse,
            status_code=status.HTTP_200_OK)
def update_system(
        system_id: str,
        data: system_schemas.SystemUpdateRequest,
        svc: Service = Depends(get_service),
):
    ValidationError.check_input_data(data.name)
    updated_system = svc.system_repository.update_system_by_id(system_id=system_id, system_name=data.name)
    ValidationError.entity_validation(updated_system, "System not found")

    return updated_system
