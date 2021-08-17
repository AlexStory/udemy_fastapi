from fastapi import APIRouter
from server.apis.v1 import route_users

router = APIRouter()

router.include_router(route_users.router, prefix="/users")
