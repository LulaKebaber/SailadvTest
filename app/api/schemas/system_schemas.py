from pydantic import BaseModel
from typing import List


class SystemCreateRequest(BaseModel):
    name: str


class SystemCreateResponse(BaseModel):
    id: str
    name: str


class SystemListResponse(BaseModel):
    systems: List[SystemCreateResponse]


class SystemUpdateRequest(BaseModel):
    name: str


class SystemUpdateResponse(BaseModel):
    id: str
    name: str
