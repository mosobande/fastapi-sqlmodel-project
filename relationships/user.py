from pydantic import UUID4, EmailStr
from sqlmodel import SQLModel


class UserRel(SQLModel):
    user_id: UUID4
    full_name: str
    email: EmailStr
    username: str
    role: str
    is_active: bool
    is_superuser: bool
