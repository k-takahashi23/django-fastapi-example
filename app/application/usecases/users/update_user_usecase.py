from app.infrastructure.repositories.users_repository import UpdateUserDTO, UsersRepository
from fastapi import Depends
from typing import Optional
from pydantic import BaseModel

class UpdateUserRequest(BaseModel):
    user_id: Optional[str] = None
    user_name: Optional[str] = None
    email: Optional[str] = None


class UpdateUserUsecase:
    def __init__(self, users_repository: UsersRepository = Depends()):
        self.users_repository = users_repository

    async def invoke(self, req: UpdateUserRequest):
        updateUserDTO = UpdateUserDTO(
            **{
                "user_id": req.user_id, 
                "user_name": req.user_name,
                "email": req.email,
            }
        )
        updatedUser = await self.users_repository.update_async(updateUserDTO)
        return updatedUser
