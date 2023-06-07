from typing import Optional

from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from .abstract import Base
from sqlmodel import SQLModel, Field, table, Relationship


class User(SQLModel, Base, table=True):
    __tablename__ = 'users'

    username: str = Field(sa_column=Column(String, unique=True, index=True, nullable=False))
    password: str
    fname: str
    lname: str





