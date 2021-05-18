from typing import Optional
from pydantic import BaseModel
from app.domain.entities.user import User

class UserUpdateDTO(BaseModel):
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
        mock_user = User(**{"user_id": id,
                            "user_name": "TanakaTaro",
                            "email": "tanaka1@mail.com"})
        return mock_user

    async def add_async(self, user: User):
        print('add user OK!')
        print(user)
        return True

    async def update_async(self, dto: UserUpdateDTO):
        print('update user OK!')
        print(dto)
        return True
    
    async def delete_async(self, user_id: str):
        print('delete user OK!')
        print(user_id)
        return