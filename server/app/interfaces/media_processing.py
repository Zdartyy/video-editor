from abc import ABC, abstractmethod


class MediaProcessing(ABC):
    @abstractmethod
    async def upload_media(self, media_path: str) -> str:
        """Uploads a media file to the server and returns the path where it is stored."""
        raise NotImplementedError("Subclasses must implement upload_media method")

    @abstractmethod
    async def send_media(self) -> bytes:
        """Sends the processed media file back to the client."""
        raise NotImplementedError("Subclasses must implement send_media method")
