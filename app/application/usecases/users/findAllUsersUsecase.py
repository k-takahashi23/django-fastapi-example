from fastapi import Depends
from ....infrastructure.repositories.usersRepository import UsersRepository

class FindAllUsersUsecase:
    def __init__(self, usersRepository: UsersRepository = Depends()):
        self.usersRepository = usersRepository

    async def invoke(self):
        users = await self.usersRepository.findAllAsync()
        return [user.__dict__ for user in users]