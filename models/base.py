from datetime import datetime
from typing import Optional

from pydantic import UUID4
from sqlalchemy import func
from sqlmodel import SQLModel, Field

from db import GUID_SERVER_DEFAULT_POSTGRESQL


class Base(SQLModel):
    # id: Optional[UUID4] = Field(
    #     sa_column=Column(
    #         GUID,
    #         index=True,
    #         primary_key=True,
    #         server_default=GUID_SERVER_DEFAULT_POSTGRESQL,
    #     )
    # )
    id: Optional[UUID4] = Field(
        primary_key=True,
        index=True,
        nullable=False,
        sa_column_kwargs={
            "server_default": GUID_SERVER_DEFAULT_POSTGRESQL,
        }
    )
    updated_at: Optional[datetime] = Field(
        default=None,
        sa_column_kwargs={
            "server_default": func.now(),
            "onupdate": func.current_timestamp()
        }
    )
    created_at: Optional[datetime] = Field(default=None, sa_column_kwargs={"server_default": func.now()})
