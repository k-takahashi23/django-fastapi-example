from app.infrastructure.repositories.users_repository import UsersRepository
from fastapi import Depends
from pydantic import BaseModel


class DeleteUserRequest(BaseModel):
    user_id: str


class DeleteUserUsecase:
    def __init__(self, users_repository: UsersRepository = Depends()):
        self.users_repository = users_repository

    async def invoke(self, req: DeleteUserRequest):
        user_id = req.user_id
        await self.users_repository.delete_async(user_id)
        return
