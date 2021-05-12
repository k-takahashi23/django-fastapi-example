from typing import Optional
from pydantic import BaseModel
from ..infrastructure.usersRepository import UsersRepository
from ..domain.user import User

class GetUserRequest(BaseModel):
    user_id: str

class GetUserResponse(BaseModel):
    user_id: str
    user_name: str
    email: str
    full_name: Optional[str] = None

class CreateUserRequest(BaseModel):
    user_name: str
    password: str
    email: str
    full_name: Optional[str] = None

class CreateUserResponse(BaseModel):
    user_id: str
    user_name: str
    email: str
    full_name: Optional[str] = None


class UsersService:
    def __init__(self):
        self.usersRepository = UsersRepository()

    async def get_user(self, user_id: str):
        user = await self.usersRepository.findAsync(user_id)
        return {
            "user_id": user.user_id,
            "user_name": user.user_name,
            "email": user.email
        }

    async def create_user(self, req: CreateUserRequest):
        user = User("id", req.user_name, req.email)
        await self.usersRepository.addAsync(user)
        return {
            "user_id": user.user_id,
            "user_name": user.user_name,
            "email": user.email,
        }