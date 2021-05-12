from typing import Optional
from pydantic import BaseModel
from ...infrastructure.repositories.usersRepository import UsersRepository
from ...domain.entities.user import User

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


class CreateUserUsecase:
    def __init__(self):
        self.usersRepository = UsersRepository()

    async def invoke(self, req: CreateUserRequest):
        user = User("id", req.user_name, req.email)
        await self.usersRepository.addAsync(user)
        return {
            "user_id": user.user_id,
            "user_name": user.user_name,
            "email": user.email,
        }