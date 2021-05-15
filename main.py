from fastapi import FastAPI
from app.web.router.users_router import users_router

app = FastAPI()

app.include_router(
    users_router,
    prefix="/users",
    tags=["users"],
)