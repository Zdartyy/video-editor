from fastapi import HTTPException
from pathlib import Path
from fastapi import UploadFile
from random import uniform
import ffmpeg
from ..interfaces.media_processing import MediaProcessing
from ..repositories.media import MediaModelRepository
from ..models.media import MediaModel


class MediaProcessingImpl(MediaProcessing):
    def __init__(
        self, server_root: Path, upload_dir: Path, repository: MediaModelRepository
    ):
        self.SERVER_ROOT = server_root
        self.UPLOAD_DIR = upload_dir
        self.repository = repository

    def __extract_media_metadata(self, file_path: Path) -> dict:
        try:
            probe = ffmpeg.probe(str(file_path))
            media_streams = [s for s in probe["streams"] if s["codec_type"] == "video"]
            media_stream = media_streams[0]
            return {
                "width": int(media_stream["width"]),
                "height": int(media_stream["height"]),
                "duration": float(media_stream["duration"]),
                "codec": media_stream["codec_name"],
                "fps": eval(media_stream["r_frame_rate"]),
                "size_in_bytes": int(probe["format"]["size"]),
            }
        except ffmpeg.Error as e:
            raise ValueError(f"Error probing media: {e.stderr.decode()}")

    async def upload_media(self, file: UploadFile) -> dict:
        if not file.filename.lower().endswith(((".mp4", ".mov"))):
            raise HTTPException(
                status_code=400, detail="Only .mp4 and .mov files are allowed"
            )

        file_path = self.UPLOAD_DIR / f"{file.filename}_{uniform(0, 99999999)}.mp4"
        with open(file_path, "wb") as buffer:
            content = await file.read()
            buffer.write(content)

        metadata = self.__extract_media_metadata(file_path)

        media_model = MediaModel(
            media_name=file_path.name,
            project_id=1,  # Replace 1 with the actual project_id
            width=metadata["width"],
            height=metadata["height"],
            duration=metadata["duration"],
            codec=metadata["codec"],
            fps=metadata["fps"],
            size_in_bytes=metadata["size_in_bytes"],
        )

        self.repository.create_media_model_entry(media_model)

        return {"filename": file_path.name, "status": "uploaded"}

    async def send_media(self, media_name: str) -> bytes:

        file_path = self.UPLOAD_DIR / media_name

        if not file_path.exists():
            raise HTTPException(
                status_code=404, detail=f"Media '{media_name}' not found"
            )

        with open(file_path, "rb") as buffer:
            return buffer.read()
