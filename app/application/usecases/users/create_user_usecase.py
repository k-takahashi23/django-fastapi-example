from app.domain.entities.user import User
from app.infrastructure.repositories.users_repository import UsersRepository
from fastapi import Depends
from typing import Optional
from pydantic import BaseModel
import uuid

class CreateUserRequest(BaseModel):
    user_name: str
    password: str
    email: Optional[str] = None

class CreateUserUsecase:
    def __init__(self, usersRepository: UsersRepository = Depends()):
        self.usersRepository = usersRepository

    async def invoke(self, req: CreateUserRequest):
        user_id = str(uuid.uuid4())
        user = User(**{ "user_id": user_id, "user_name": req.user_name, "email": req.email })
        await self.usersRepository.addAsync(user)
        return user