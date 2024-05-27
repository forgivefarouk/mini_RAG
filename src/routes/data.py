from fastapi import FastAPI , APIRouter , Depends , UploadFile , status
from fastapi.responses import JSONResponse
import os
from helpers.config import Settings , get_settings
from controllers import DataController , FileController
import aiofiles
from models import ResponseSignal
import logging

logging.basicConfig(level=logging.ERROR, filename="py_log.log",filemode="a")




data_route = APIRouter(
    prefix = "/api/v1/data",
    tags=["api-v1","data"]
)

@data_route.post("/upload/{file_id}")
async def upload(file_id : str, file : UploadFile, app_settings : Settings = Depends(get_settings)):
    
    #validate file properties
    is_valid , signal_type = DataController().validate_upload_file(file)
    
    if not is_valid:
        logging.error('Bad Request 400')

        return JSONResponse(
            status_code = status.HTTP_400_BAD_REQUEST ,
            content={
                "signal": signal_type
            }
        )
        
    #upload file in directory
    upload_dir = FileController().get_file_path(file_id=file_id)
    file_path = os.path.join(
        upload_dir,
        file.filename
    )
    
    try:
    
        async with aiofiles.open(file_path,"wb") as f:
            while chunk := await file.read(app_settings.FILE_CHUNK_SIZE):
                await f.write(chunk)
    except Exception as e:
        logging.error(f"Error when uploading File {e}")
              
        return JSONResponse(
        status_code = status.HTTP_400_BAD_REQUEST ,
        content={
            "signal": ResponseSignal.FILE_UPLOAD_FAILED.vlaue
        }
        )
        
    logging.info("An INFO")

    return JSONResponse(
        content={
            "signal": ResponseSignal.FILE_UPLOAD_SUCCESS.value
        }
        )
    
    

    
