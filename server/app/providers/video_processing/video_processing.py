from pathlib import Path
from ...services.video_processing.video_processing import VideoProcessingImpl

class VideoProcessingProvider:
    SERVER_ROOT = Path(__file__).parent.parent.parent.parent
    UPLOAD_DIR = SERVER_ROOT / "uploaded_videos"
    
    @classmethod
    def get_video_processing(cls) -> VideoProcessingImpl:
        cls.UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
        return VideoProcessingImpl(server_root=cls.SERVER_ROOT, upload_dir=cls.UPLOAD_DIR)