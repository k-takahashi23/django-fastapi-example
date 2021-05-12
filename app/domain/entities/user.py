from pydantic.dataclasses import dataclass
from typing import Optional

@dataclass
class User:
    user_id: str
    user_name: str
    email: Optional[str] = None