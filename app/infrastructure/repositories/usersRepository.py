from ...domain.entities.user import User

class UsersRepository:
  def __init__(self):
    pass

  async def findAllAsync(self) -> list[User]:
    mockUsers = [
      User("id1", "TanakaTaro", "tanaka1@mail.com"),
      User("id2", "TanakaJiro", "tanaka2@mail.com")
    ]
    return mockUsers

  async def findAsync(self, id: str) -> User:
    mockUser = User(id, "TanakaTaro", "tanaka@mail.com")
    return mockUser

  async def addAsync(self, user: User) -> bool:
    print('add user OK!')
    return True