from fastapi import APIRouter, UploadFile, Depends

from app.services.video_processing.video_processing import VideoProcessingImpl
from ...providers.video_processing.video_processing import VideoProcessingProvider

router = APIRouter()

@router.post("/upload-video")
async def upload_video(
    file: UploadFile,
    video_processing: VideoProcessingImpl = Depends(VideoProcessingProvider.get_video_processing)
):
    return await video_processing.upload_video(file)