from ..models.media import MediaModel
from sqlalchemy.orm import Session


class MediaModelRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_media_model_entry(
        self,
        model: MediaModel,
    ) -> MediaModel:
        self.db.add(model)
        self.db.commit()
        self.db.refresh(model)
        return model
