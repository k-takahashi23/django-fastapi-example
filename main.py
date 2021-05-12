from fastapi import FastAPI
from app.application.users.createUserUsecase import CreateUserRequest, CreateUserResponse, CreateUserUsecase
from app.application.users.getUserUsecase import GetUserResponse, GetUserUsecase

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/users/{user_id}", response_model=GetUserResponse)
async def get_user(user_id: str):
    usecase = GetUserUsecase()
    return await usecase.invoke(user_id)

@app.post("/users", response_model=CreateUserResponse)
async def create_user(req: CreateUserRequest):
    usecase = CreateUserUsecase()
    return await usecase.invoke(req)