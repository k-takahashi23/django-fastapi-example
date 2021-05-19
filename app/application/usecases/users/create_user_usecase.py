from app.infrastructure.repositories.users_repository import AddUserDTO, UsersRepository
from fastapi import Depends
from typing import Optional
from pydantic import BaseModel


class CreateUserRequest(BaseModel):
    user_name: str
    password: str
    email: Optional[str] = None


class CreateUserUsecase:
    def __init__(self, users_repository: UsersRepository = Depends()):
        self.users_repository = users_repository

    async def invoke(self, req: CreateUserRequest):
        addUserDTO = AddUserDTO(
            **{
                "password": req.password,
                "user_name": req.user_name,
                "email": req.email,
            }
        )
        addedUser = await self.users_repository.add_async(addUserDTO)
        return addedUser
