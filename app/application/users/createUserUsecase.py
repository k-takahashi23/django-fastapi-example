from fastapi import Depends
from typing import Optional
from pydantic import BaseModel
from ...infrastructure.repositories.usersRepository import UsersRepository
from ...domain.entities.user import User

class CreateUserRequest(BaseModel):
    user_name: str
    password: str
    email: Optional[str] = None

class CreateUserResponse(BaseModel):
    user_id: str
    user_name: str
    email: Optional[str] = None

class CreateUserUsecase:
    def __init__(self, usersRepository: UsersRepository = Depends()):
        self.usersRepository = usersRepository

    async def invoke(self, req: CreateUserRequest):
        user_id = "id"
        user = User(user_id, req.user_name, req.email)
        await self.usersRepository.addAsync(user)
        return user.__dict__