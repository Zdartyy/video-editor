from pydantic import BaseModel, Field


class ProjectCreateRequest(BaseModel):
    project_name: str = Field(..., min_length=1, max_length=50)


class ProjectCreateResponse(BaseModel):
    project_id: int
    project_name: str
