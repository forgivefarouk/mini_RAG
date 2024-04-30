from fastapi import FastAPI , APIRouter
import os

base_route = APIRouter(
    prefix = "/api/v1",
    tags=["api-v1"]
)


@base_route.get('/')
async def welcome():
    app_name = os.getenv("APP_NAME")
    version_name=os.getenv("APP_VERSION")
    return {
        "app name" : app_name,
        "version name": version_name,
    }
