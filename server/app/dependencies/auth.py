from fastapi import Header, HTTPException, Depends
from ..models.user import UserModel
from ..repositories.user import UserModelRepository
from ..providers.user import UserProvider


async def get_current_user(
    api_key: str = Header(..., alias="API-Key"),
    user_repository: UserModelRepository = Depends(UserProvider.get_repository),
) -> UserModel:

    user = user_repository.get_user_by_api_key(api_key)

    if not user:
        raise HTTPException(status_code=401, detail="Invalid API Key")

    return user
