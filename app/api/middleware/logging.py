from fastapi import Request
from app.api.services.db_service import SessionDB
from app.api.repositories.log_repository import LogRepository


# async def record_logs_middleware(
#     request: Request,
#     call_next,
# ):
#     response = await call_next(request)
#     svc: Service = get_service()
#
#     client_ip = request.client.host
#     http_method = request.method
#     endpoint = request.url.path
#     svc.log_repository.record_log(client_ip, endpoint, http_method)
#
#     return response

async def record_logs_middleware(
        request: Request, call_next
):
    response = await call_next(request)

    client_ip = request.client.host
    http_method = request.method
    endpoint = request.url.path

    log_repository = LogRepository(SessionDB)
    log_repository.record_log(client_ip, endpoint, http_method)

    return response
