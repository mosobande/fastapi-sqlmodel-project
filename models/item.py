from typing import Optional, TYPE_CHECKING

from pydantic import UUID4
from sqlalchemy.orm import declared_attr, synonym
from sqlmodel import SQLModel, Field, Relationship

from relationships import UserRel
from .base import Base

if TYPE_CHECKING:
    from .user import User


class ItemBase(SQLModel):
    title: str = Field(index=True)
    description: str = Field(index=True)
    owner_id: UUID4 = Field(foreign_key="users.id", nullable=False, index=True)


class Item(Base, ItemBase, table=True):
    __tablename__ = "items"

    owner: Optional["User"] = Relationship(back_populates="items")

    @declared_attr
    def item_id(self):
        return synonym("id")


class ItemCreate(ItemBase):
    pass


class ItemRead(ItemBase):
    item_id: UUID4
    owner: UserRel


class ItemUpdate(ItemBase):
    pass
