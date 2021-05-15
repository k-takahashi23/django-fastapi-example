from app.application.usecases.users.user import User
from app.infrastructure.repositories.users_repository import UsersRepository
from fastapi import Depends

class FindAllUsersUsecase:
    def __init__(self, usersRepository: UsersRepository = Depends()):
        self.usersRepository = usersRepository

    async def invoke(self):
        users = await self.usersRepository.findAllAsync()
        return [User.from_domain_model(user) for user in users]