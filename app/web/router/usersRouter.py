from app.application.usecases.users.createUserUsecase import CreateUserRequest, CreateUserUsecase
from app.application.usecases.users.findAllUsersUsecase import FindAllUsersUsecase
from app.application.usecases.users.findUserUsecase import FindUserRequest, FindUserUsecase
from app.application.usecases.users.user import User
from typing import List
from fastapi import APIRouter, Depends

usersRouter = APIRouter()

@usersRouter.get("", response_model=List[User])
async def find_user(usecase: FindAllUsersUsecase = Depends()):
    return await usecase.invoke()

@usersRouter.get("/{user_id}", response_model=User)
async def find_user(user_id: str, usecase: FindUserUsecase = Depends()):
    req = FindUserRequest(user_id=user_id)
    return await usecase.invoke(req)

@usersRouter.post("", response_model=User)
async def create_user(req: CreateUserRequest, usecase: CreateUserUsecase = Depends()):
    return await usecase.invoke(req)