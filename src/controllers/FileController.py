from .BaseController import BaseController
import os

class FileController(BaseController):
    
    def __init__(self):
        super().__init__()
        
    def get_file_path(self , file_id:str):
        
        _file_path = os.path.join(
            self.files_path,
            file_id
        )
        
        if not os.path.exists(_file_path):
            os.makedirs(_file_path)
            
        return _file_path
