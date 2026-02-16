from fastapi import APIRouter
from .media_processing import router as media_processing_router
from .user import router as user_router

api_router = APIRouter()
api_router.include_router(media_processing_router)
api_router.include_router(user_router)
