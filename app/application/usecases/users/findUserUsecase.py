from fastapi import Depends
from pydantic import BaseModel
from ....infrastructure.repositories.usersRepository import UsersRepository

class FindUserRequest(BaseModel):
    user_id: str

class FindUserUsecase:
    def __init__(self, usersRepository: UsersRepository = Depends()):
        self.usersRepository = usersRepository

    async def invoke(self, req: FindUserRequest):
        user = await self.usersRepository.findAsync(req.user_id)
        return user.__dict__