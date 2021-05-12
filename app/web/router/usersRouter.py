from fastapi import APIRouter, Depends
from app.application.usecases.users.createUserUsecase import CreateUserRequest, CreateUserResponse, CreateUserUsecase
from app.application.usecases.users.getUserUsecase import GetUserRequest, GetUserResponse, GetUserUsecase

usersRouter = APIRouter()

@usersRouter.get("/{user_id}", response_model=GetUserResponse)
async def get_user(user_id: str, usecase: GetUserUsecase = Depends()):
    req = GetUserRequest(user_id=user_id)
    return await usecase.invoke(req)

@usersRouter.post("", response_model=CreateUserResponse)
async def create_user(req: CreateUserRequest, usecase: CreateUserUsecase = Depends()):
    return await usecase.invoke(req)