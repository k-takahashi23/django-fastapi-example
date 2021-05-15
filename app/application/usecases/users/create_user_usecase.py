from app.application.usecases.users.user import User
from app.domain.entities.user import User as DomainModelUser
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
        user = DomainModelUser(user_id, req.user_name, req.email)
        await self.usersRepository.addAsync(user)
        return User.from_domain_model(user)