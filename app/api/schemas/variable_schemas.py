from pydantic import BaseModel
from typing import List


class VariableCreateRequest(BaseModel):
    system_id: str
    name: str
    type: str


class VariableCreateResponse(BaseModel):
    id: str
    system_id: str
    name: str
    type: str


class VariableListResponse(BaseModel):
    variables: List[VariableCreateResponse]


class VariableUpdateRequest(BaseModel):
    system_id: str
    name: str
    type: str


class VariableUpdateResponse(BaseModel):
    id: str
    system_id: str
    name: str
    type: str