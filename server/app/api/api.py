from fastapi import APIRouter
from .video_processing import router as video_processing_router
from .user import router as user_router
from .project import router as project_router

api_router = APIRouter()
api_router.include_router(video_processing_router)
api_router.include_router(user_router)
api_router.include_router(project_router)
