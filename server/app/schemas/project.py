from pydantic import BaseModel, Field
from datetime import datetime


class ProjectCreateRequest(BaseModel):
    project_name: str = Field(..., min_length=1, max_length=50)


class ProjectCreateResponse(BaseModel):
    project_id: int
    project_name: str
    created_at: datetime
