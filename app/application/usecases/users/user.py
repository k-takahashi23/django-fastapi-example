from app.domain.entities.user import User as DomainUser
from typing import Optional
from pydantic.main import BaseModel

class User(BaseModel):
    user_id: str
    user_name: str
    email: Optional[str] = None

    @staticmethod
    def from_domain_model(domain_model: DomainUser):
        return User(
            user_id=domain_model.user_id,
            user_name = domain_model.user_name,
            email = domain_model.email
        )