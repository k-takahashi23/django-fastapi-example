from fastapi import FastAPI
from app.web.router.users_router import usersRouter

app = FastAPI()

app.include_router(
    usersRouter,
    prefix="/users",
    tags=["users"],
)