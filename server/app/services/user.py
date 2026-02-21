from app.error_handler.error_handler import AlreadyExistsError

from ..interfaces.user import User
from ..repositories.user import UserModelRepository
from ..models.user import UserModel
import secrets
import hashlib
from collections import namedtuple


class UserImpl(User):
    def __init__(self, repository: UserModelRepository):
        self.repository = repository

    user_response = namedtuple("UserResponse", ["username", "api_key"])

    async def register_user(self, username: str) -> user_response:
        existing_user = self.repository.get_user_by_username(username)

        if existing_user:
            raise AlreadyExistsError(f"User with username '{username}' already exists")

        api_key = f"{username}_{secrets.token_urlsafe(32)}"
        hashed_api_key = hashlib.sha256(api_key.encode()).hexdigest()

        user = UserModel(username=username, api_key=hashed_api_key)

        created_user = self.repository.create_user_model_entry(user)

        return self.user_response(username=created_user.username, api_key=api_key)
