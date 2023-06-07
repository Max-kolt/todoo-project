import logging
from typing import TypeVar, Optional
from pydantic import BaseModel
from datetime import date

from src.models import User

T = TypeVar('T')

logger = logging.getLogger(__name__)


class RegisterSchema(BaseModel):
    username: str
    fname: str
    lname: str
    password: str


class LoginSchema(BaseModel):
    username: str
    password: str


class RecordSchema(BaseModel):
    id: str = None
    name: str
    description: str
    complited: bool = None
    deadline: date
    archive: bool = None
    user: Optional[User]


class DetailSchema(BaseModel):
    status: str
    message: str
    result: Optional[T] = None


class ResponseSchema(BaseModel):
    detail: str
    result: Optional[T] = None
