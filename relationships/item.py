from pydantic import UUID4
from sqlmodel import SQLModel


class ItemRel(SQLModel):
    item_id: UUID4
    title: str
    description: str
