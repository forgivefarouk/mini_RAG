from fastapi import FastAPI , APIRouter , Depends
import os
from helpers.config import Settings , get_settings
base_route = APIRouter(
    prefix = "/api/v1",
    tags=["api-v1"]
)


@base_route.get('/')
async def welcome(app_settings : Settings = Depends(get_settings)):
    app_name = app_settings.APP_NAME
    version_name = app_settings.APP_VERSION
    return {
        "app name" : app_name,
        "version name": version_name,
    }
