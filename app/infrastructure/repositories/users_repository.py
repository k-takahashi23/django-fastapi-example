from app.domain.entities.user import User

class UsersRepository:
  def __init__(self):
    pass

  async def findAllAsync(self) -> list[User]:
    mockUsers = [
      User(**{ "user_id": "id1", "user_name": "TanakaTaro", "email": "tanaka1@mail.com" }),
      User(**{ "user_id": "id2", "user_name": "TanakaJiro", "email": "tanaka2@mail.com" })
    ]
    return mockUsers

  async def findAsync(self, id: str) -> User:
    mockUser = User(**{ "user_id": id, "user_name": "TanakaTaro", "email": "tanaka1@mail.com" })
    return mockUser

  async def addAsync(self, user: User) -> bool:
    print('add user OK!')
    return True