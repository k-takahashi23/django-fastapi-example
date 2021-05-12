from fastapi import APIRouter, Depends
from app.application.users.createUserUsecase import CreateUserRequest, CreateUserResponse, CreateUserUsecase
from app.application.users.getUserUsecase import GetUserResponse, GetUserUsecase

usersRouter = APIRouter()

@usersRouter.get("/{user_id}", response_model=GetUserResponse)
async def get_user(user_id: str, usecase: GetUserUsecase = Depends()):
    return await usecase.invoke(user_id)

@usersRouter.post("", response_model=CreateUserResponse)
async def create_user(req: CreateUserRequest, usecase: CreateUserUsecase = Depends()):
    return await usecase.invoke(req)