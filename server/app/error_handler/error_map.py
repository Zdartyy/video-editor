from fastapi import status
from app.error_handler.error_handler import FfmpegError, FfmpegError, NotFoundError, ValidationError

ERROR_MAP = {
    NotFoundError: status.HTTP_404_NOT_FOUND,
    ValidationError: status.HTTP_400_BAD_REQUEST,
    FfmpegError: status.HTTP_500_INTERNAL_SERVER_ERROR,
}