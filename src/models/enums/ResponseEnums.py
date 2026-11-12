from enum import Enum

class ResponseSignal(Enum):


    FILE_VALIDATED_SUCCESS = "File validated successfully"
    FILE_TYPE_NOT_SUPPORTED = "File type not supported"
    FILE_SIZE_EXCEEDS_LIMIT = "File size exceeds the limit"
    FILE_UPLOAD_SUCCESS = "File uploaded successfully"
    FILE_UPLOAD_FAILED = "File upload failed"
    FILE_PROCESSING_FAILED = "File processing failed"
    FILE_PROCESSING_SUCCESS = "File processed successfully"
    NO_FILES_ERROR = "not found files"
    FILE_ID_ERROR = "no file found with this id"
    
