from pydantic import BaseModel, Field


class UserRegisterRequest(BaseModel):
    username: str = Field(..., min_length=3, max_length=20)


class UserRegisterResponse(BaseModel):
    username: str
    api_key: str
