from typing import Optional
import uuid
from pydantic import BaseModel
from app.domain.entities.user import User


class AddUserDTO(BaseModel):
    user_name: str
    password: str
    email: Optional[str] = None


class UpdateUserDTO(BaseModel):
    user_id: Optional[str] = None
    user_name: Optional[str] = None
    email: Optional[str] = None


class UsersRepository:
    def __init__(self):
        pass

    async def find_alll_async(self) -> list[User]:
        mock_users = [
            User(**{"user_id": "id1", "user_name": "TanakaTaro", "email": "tanaka1@mail.com"}),
            User(**{"user_id": "id2", "user_name": "TanakaJiro", "email": "tanaka2@mail.com"})
        ]
        return mock_users

    async def find_async(self, id: str) -> User:
        mock_user = User(**{
            "user_id": id,
            "user_name": "TanakaTaro",
            "email": "tanaka1@mail.com"
        })
        return mock_user

    async def add_async(self, dto: AddUserDTO) -> User:
        print('add user OK!')
        user_id = str(uuid.uuid4())
        print(user_id, dto)
        user = User(**{
            "user_id": user_id,
            "user_name": dto.user_name,
            "email": dto.email
        })
        return user

    async def update_async(self, dto: UpdateUserDTO) -> User:
        print('update user OK!')
        print(dto)
        user = User(**{
            "user_id": dto.user_id,
            "user_name": dto.user_name,
            "email": dto.email
        })
        return user

    async def delete_async(self, user_id: str) -> None:
        print('delete user OK!')
        print(user_id)
        return
