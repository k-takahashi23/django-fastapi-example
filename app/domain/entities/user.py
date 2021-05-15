from typing import Optional
from pydantic.main import BaseModel


class User(BaseModel):
    user_id: str
    user_name: str
    email: Optional[str] = None
