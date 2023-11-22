from pydantic import BaseModel


class SystemLogResponse(BaseModel):
    id: str
    timestamp: str
    ip_address: str
    endpoint: str
    http_method: str


class SystemLogsResponse(BaseModel):
    logs: list[SystemLogResponse]