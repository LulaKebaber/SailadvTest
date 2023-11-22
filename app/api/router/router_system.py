from fastapi import Depends, HTTPException, status

from ..services.db_service import Service, get_service
from . import router
from ..schemas import system_schemas, log_schemas


@router.get("/system", response_model=system_schemas.SystemListResponse, status_code=status.HTTP_200_OK)
def get_systems(
        svc: Service = Depends(get_service)
):
    systems = svc.system_repository.get_all_systems()
    if not systems:
        raise HTTPException(status_code=404, detail="No systems found")

    return {"systems": systems}


@router.post("/system", response_model=system_schemas.SystemCreateResponse, status_code=status.HTTP_201_CREATED)
def add_new_system(
        data: system_schemas.SystemCreateRequest,
        svc: Service = Depends(get_service),
):
    new_system = svc.system_repository.add_new_system(system_name=data.name)
    if not new_system:
        raise HTTPException(status_code=404, detail="Bad request")

    return new_system


@router.delete("/system/{system_id:str}", status_code=status.HTTP_200_OK)
def delete_system(
        system_id: str,
        svc: Service = Depends(get_service),
):
    deleted_system = svc.system_repository.delete_system_by_id(system_id=system_id)
    if not deleted_system:
        raise HTTPException(status_code=404, detail="System not found")
    return deleted_system


@router.put("/system/{system_id:str}", response_model=system_schemas.SystemUpdateResponse,
            status_code=status.HTTP_200_OK)
def update_system(
        system_id: str,
        data: system_schemas.SystemUpdateRequest,
        svc: Service = Depends(get_service),
):
    updated_system = svc.system_repository.update_system_by_id(system_id=system_id, system_name=data.name)
    if not updated_system:
        raise HTTPException(status_code=404, detail="System not found")
    return updated_system


@router.get("/system/logs", response_model=log_schemas.SystemLogsResponse, status_code=status.HTTP_200_OK)
def get_system_logs(
        svc: Service = Depends(get_service),
):
    logs = svc.log_repository.get_system_logs()
    if not logs:
        raise HTTPException(status_code=404, detail="No logs found")
    return {"logs": logs}