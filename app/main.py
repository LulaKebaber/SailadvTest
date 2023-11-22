from fastapi import FastAPI

from app.api.router import router
from app.api.middleware.logging import record_logs_middleware


app = FastAPI()

app.include_router(router, prefix="/api", tags=["api"])
app.middleware("http")(record_logs_middleware)
