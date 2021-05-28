from app.infrastructure.repositories.users_repository import UsersRepository
from fastapi import Depends
from pydantic import BaseModel


class FindUserRequest(BaseModel):
    user_id: str


class FindUserUsecase:
    def __init__(self, users_repository: UsersRepository = Depends()):
        self.users_repository = users_repository

    async def invoke(self, req: FindUserRequest):
        user = await self.users_repository.find_async(req.user_id)
        return user;
