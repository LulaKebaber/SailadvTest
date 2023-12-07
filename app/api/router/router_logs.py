from fastapi import Depends, status

from ..services.db_service import Service, get_service
from ..schemas import log_schemas
from . import router
from ..utils.validation import ValidationError


@router.get("/logs", response_model=log_schemas.SystemLogsResponse, status_code=status.HTTP_200_OK)
def get_system_logs(
        svc: Service = Depends(get_service),
):
    logs = svc.log_repository.get_system_logs()
    ValidationError.entity_validation(logs, "No logs found")

    return {"logs": logs}