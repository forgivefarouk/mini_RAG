from enum import Enum

class ResponseSignal(Enum):
    
    FILE_TYPE_NOT_SUPPORTED ="File_type_not_supported"
    FILE_SIZE_EXCEEDED = "File_size_exceeded"
    FILE_UPLOAD_SUCCESS="file_upload_success"
    FILE_UPLOAD_FAILED="file_upload_failed"
    FILE_VALIDATED_SUCCESS="file_validated_success"