from app.infrastructure.repositories.users_repository import UsersRepository
from fastapi import Depends


class FindAllUsersUsecase:
    def __init__(self, users_repository: UsersRepository = Depends()):
        self.users_repository = users_repository

    async def invoke(self):
        users = await self.users_repository.find_alll_async()
        return users
