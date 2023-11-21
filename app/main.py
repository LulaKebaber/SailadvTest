from fastapi import FastAPI

from app.api.router import router as auth_router

app = FastAPI()

app.include_router(auth_router, prefix="/api", tags=["api"])