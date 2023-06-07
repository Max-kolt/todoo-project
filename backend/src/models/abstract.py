from datetime import datetime
from typing import Optional

from sqlalchemy import Column, DateTime
from pydantic import BaseModel
from sqlmodel import Field


class Base(BaseModel):
    id: Optional[str] = Field(None, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.now)
    modified_at: datetime = Field(sa_column=Column(DateTime, default=datetime.now(),
                                                   onupdate=datetime.now(), nullable=False))
