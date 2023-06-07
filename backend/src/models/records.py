
from sqlalchemy.orm import relationship, backref
from datetime import date
from typing import Optional

from sqlmodel import Field, Relationship, SQLModel

from .abstract import Base


class Record(SQLModel, Base, table=True):
    __tablename__ = 'records'

    name: str
    description: str
    complited: bool
    deadline: date
    archive: bool

    user_id: Optional[str] = Field(default=None, foreign_key='users.id')
