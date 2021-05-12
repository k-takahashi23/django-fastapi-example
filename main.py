from fastapi import FastAPI
from app.web.router.usersRouter import usersRouter

app = FastAPI()

app.include_router(
    usersRouter,
    prefix="/users",
    tags=["users"],
)