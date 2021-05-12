from fastapi import APIRouter, Depends
from app.application.usecases.users.createUserUsecase import CreateUserRequest, CreateUserResponse, CreateUserUsecase
from app.application.usecases.users.findUserUsecase import FindUserRequest, FindUserResponse, FindUserUsecase

usersRouter = APIRouter()

@usersRouter.get("/{user_id}", response_model=FindUserResponse)
async def find_user(user_id: str, usecase: FindUserUsecase = Depends()):
    req = FindUserRequest(user_id=user_id)
    return await usecase.invoke(req)

@usersRouter.post("", response_model=CreateUserResponse)
async def create_user(req: CreateUserRequest, usecase: CreateUserUsecase = Depends()):
    return await usecase.invoke(req)