
from sqlalchemy.orm import Session
from typing import Optional, List, Any
from ..models.system import System
from ..models.log import Log
from datetime import datetime, timezone


class LogRepository:
    def __init__(self, database: Session):
        self.database = database

    def record_log(self, ip_address: str, endpoint: str, http_method: str):
        log = Log(
            timestamp=datetime.now(timezone.utc),
            ip_address=ip_address,
            endpoint=endpoint,
            http_method=http_method,
        )
        self.database.add(log)
        self.database.commit()
        self.database.refresh(log)
        return {"detail": "Log recorded"}

    def get_system_logs(self) -> List[Any]:
        logs = self.database.query(Log).all()
        if not logs:
            return []
        return [{
            'id': str(log.id),
            'timestamp': str(log.timestamp),
            'ip_address': log.ip_address,
            'endpoint': log.endpoint,
            'http_method': log.http_method,
        } for log in logs]

