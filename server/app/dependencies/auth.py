from fastapi import Header, HTTPException, Depends
from sqlalchemy.orm import Session
from ..database import get_db_session
from ..models.user import UserModel
from ..repositories.user import UserModelRepository


async def get_current_user(
    api_key: str = Header(..., alias="API-Key"),
    db: Session = Depends(get_db_session),
) -> UserModel:
    
    user_repository = UserModelRepository(db)
    user = user_repository.get_user_by_api_key(api_key)

    if not user:
        raise HTTPException(status_code=401, detail="Invalid API Key")
    
    return user