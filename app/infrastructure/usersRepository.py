from ..domain.user import User

class UsersRepository:
  def __init__(self):
    pass

  async def findAsync(self, id: str) -> User:
    mockUser = User(id, "TanakaTaro", "tanaka@mail.com")
    return mockUser

  async def addAsync(self, user: User) -> bool:
    print('add user OK!')
    return True