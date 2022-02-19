from typing import Optional, List, TYPE_CHECKING

from pydantic import EmailStr, UUID4
from sqlalchemy.orm import declared_attr, synonym
from sqlmodel import SQLModel, Field, Relationship

from relationships import ItemRel
from .base import Base

if TYPE_CHECKING:
    from .item import Item


class UserBase(SQLModel):
    full_name: Optional[str] = Field(default=None, index=True)
    email: EmailStr = Field(index=True, sa_column_kwargs={"unique": True})
    username: str = Field(index=True, sa_column_kwargs={"unique": True})
    role: str = Field(default="reader")
    secret: str = Field(index=True, sa_column_kwargs={"unique": True})
    is_active: bool = Field(default=False)
    is_superuser: bool = Field(default=False)

    # class Config:
    #     fields = {
    #         'id': {'alias': 'user_id'}
    #     }


class User(Base, UserBase, table=True):
    __tablename__ = "users"

    items: Optional["Item"] = Relationship(
        sa_relationship_kwargs={
            "back_populates": "owner"
        }
    )

    @declared_attr
    def user_id(self):
        return synonym("id")


class UserRel(SQLModel):
    full_name: str
    email: EmailStr
    username: str
    role: str
    is_active: bool
    is_superuser: bool


class UserCreate(UserBase):
    pass


class UserRead(UserBase):
    user_id: UUID4
    items: List[ItemRel]


class UserUpdate(UserBase):
    pass
