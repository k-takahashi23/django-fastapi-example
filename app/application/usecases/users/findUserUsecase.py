from fastapi import Depends
from typing import Optional
from pydantic import BaseModel
from ....infrastructure.repositories.usersRepository import UsersRepository
from ....domain.entities.user import User

class FindUserRequest(BaseModel):
    user_id: str

class FindUserResponse(BaseModel):
    user_id: str
    user_name: str
    email: Optional[str] = None

class FindUserUsecase:
    def __init__(self, usersRepository: UsersRepository = Depends()):
        self.usersRepository = usersRepository

    async def invoke(self, req: FindUserRequest):
        user = await self.usersRepository.findAsync(req.user_id)
        return user.__dict__