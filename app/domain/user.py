from pydantic.dataclasses import dataclass

@dataclass
class User:
    user_id: str
    user_name: str
    email: str