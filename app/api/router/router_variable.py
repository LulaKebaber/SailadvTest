from fastapi import Depends, HTTPException, status

from ..services.db_service import Service, get_service
from . import router
from ..schemas import variable_schemas
from ..utils.validation import ValidationError


@router.get("/variable", response_model=variable_schemas.VariableListResponse, status_code=status.HTTP_200_OK)
def get_variables(
        svc: Service = Depends(get_service)
):
    variables = svc.variable_repository.get_all_variables()
    ValidationError.entity_validation(variables, "No variables found")

    return {"variables": variables}


@router.post("/variable", response_model=variable_schemas.VariableCreateResponse, status_code=status.HTTP_201_CREATED)
def add_new_variable(
        data: variable_schemas.VariableCreateRequest,
        svc: Service = Depends(get_service),
):
    ValidationError.check_input_data(data.system_id, data.name, data.type)
    if not svc.system_repository.get_system_by_id(data.system_id):
        raise HTTPException(status_code=404, detail="System not found")

    new_variable = svc.variable_repository.add_new_variable(
        system_id=data.system_id,
        name=data.name,
        type=data.type,
    )
    ValidationError.entity_validation(new_variable, "Variable not created")

    return new_variable


@router.delete("/variable/{variable_id:str}", status_code=status.HTTP_200_OK)
def delete_variable(
        variable_id: str,
        svc: Service = Depends(get_service),
):
    if not svc.variable_repository.get_variable_by_id(variable_id):
        raise HTTPException(status_code=404, detail="Variable not found")

    variable_deleted = svc.variable_repository.delete_variable_by_id(variable_id=variable_id)
    ValidationError.entity_validation(variable_deleted, "Variable not deleted")

    return variable_deleted


@router.put("/variable/{variable_id:str}", response_model=variable_schemas.VariableUpdateResponse,
            status_code=status.HTTP_200_OK)
def update_variable(
        variable_id: str,
        data: variable_schemas.VariableUpdateRequest,
        svc: Service = Depends(get_service),
):
    ValidationError.check_input_data(data.name, data.type, data.system_id)
    if not svc.variable_repository.get_variable_by_id(variable_id):
        raise HTTPException(status_code=404, detail="Variable not found")

    variable_updated = svc.variable_repository.update_variable_by_id(
        variable_id=variable_id,
        name=data.name,
        type=data.type,
        system_id=data.system_id,
    )

    return variable_updated
