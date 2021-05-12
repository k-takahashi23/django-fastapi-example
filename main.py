from fastapi import FastAPI
from app.application.usersService import GetUserResponse, CreateUserRequest, CreateUserResponse, UsersService

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/users/{user_id}", response_model=GetUserResponse)
async def get_user(user_id: str):
    usersService = UsersService()
    return await usersService.get_user(user_id)

@app.post("/users", response_model=CreateUserResponse)
async def create_user(req: CreateUserRequest):
    usersService = UsersService()
    return await usersService.create_user(req)