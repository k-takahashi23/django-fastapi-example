from app.application.usecases.users.user import User
from app.infrastructure.repositories.users_repository import UsersRepository
from fastapi import Depends
from pydantic import BaseModel

class FindUserRequest(BaseModel):
    user_id: str

class FindUserUsecase:
    def __init__(self, usersRepository: UsersRepository = Depends()):
        self.usersRepository = usersRepository

    async def invoke(self, req: FindUserRequest):
        user = await self.usersRepository.findAsync(req.user_id)
        return User.from_domain_model(user)