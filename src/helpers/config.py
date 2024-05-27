
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME : str
    APP_VERSION : str
    OPENAI_API_KEY : str
    
    FILE_ALLOWED_TYPES: list
    FILE_MAX_SIZE : int
    FILE_CHUNK_SIZE : int
    
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        
        
def get_settings():
    return Settings()