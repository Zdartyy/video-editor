from fastapi import HTTPException
from pathlib import Path
from fastapi import UploadFile
from random import uniform
from ...interfaces.video_processing.video_processing import VideoProcessing

class VideoProcessingImpl(VideoProcessing):
    def __init__(self, server_root: Path, upload_dir: Path):
        self.SERVER_ROOT = server_root
        self.UPLOAD_DIR = upload_dir
    
    async def upload_video(self, file: UploadFile) -> dict:
        if not file.filename.lower().endswith(((".mp4", ".mov"))):
            raise HTTPException(status_code=400, detail="Only .mp4 and .mov files are allowed")
        
        file_path = self.UPLOAD_DIR / f"{file.filename}_{uniform(0, 99999999)}.mp4"
        with open(file_path, "wb") as buffer:
            content = await file.read()
            buffer.write(content)

        return {"filename": file_path.name, "status": "uploaded"}
    
    async def send_video(self) -> bytes:
        # Implementation for sending video back to client
        pass