from fastapi import APIRouter

from app.presentation.http.controllers.general.router import general_router

api_v1_router = APIRouter(
    prefix="/api/v1",
)


api_v1_sub_routers: tuple[APIRouter, ...] = (general_router,)

for router in api_v1_sub_routers:
    api_v1_router.include_router(router)
