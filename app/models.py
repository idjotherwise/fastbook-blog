from sqlmodel import SQLModel, Field
from typing import Optional


class BookBase(SQLModel):
    title: str
    author: Optional[str]
    # new ---
    description: Optional[str]
    # -------


class Book(BookBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)


class BookCreate(BookBase):
    pass


class BookRead(BookBase):
    id: int