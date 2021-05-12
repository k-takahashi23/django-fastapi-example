from fastapi import Depends
from typing import Optional
from pydantic import BaseModel
from ...infrastructure.repositories.usersRepository import UsersRepository
from ...domain.entities.user import User

class GetUserResponse(BaseModel):
    user_id: str
    user_name: str
    email: str
    full_name: Optional[str] = None

class GetUserUsecase:
    def __init__(self, usersRepository: UsersRepository = Depends()):
        self.usersRepository = usersRepository

    async def invoke(self, user_id: str):
        user = await self.usersRepository.findAsync(user_id)
        return {
            "user_id": user.user_id,
            "user_name": user.user_name,
            "email": user.email
        }