from typing import Generic, TypeVar
from sqlalchemy import update, delete
from sqlalchemy.future import select
from config import db, commit_rollback

T = TypeVar('T')


class BaseRepo:
    model = Generic[T]

    @classmethod
    async def create(cls, **kwargs):
        model = cls.model(**kwargs)
        db.add(model)
        await commit_rollback()
        return model

    @classmethod
    async def update(cls, model_id: str, **kwargs):
        query = update(cls.model)\
            .where(cls.model.id == model_id)\
            .values(**kwargs)\
            .execution_options(synchronize_session='fetch')
        await db.execute(query)
        await commit_rollback()

    @classmethod
    async def delete(cls, model_id: str):
        query = delete(cls.model).where(cls.model.id == model_id)
        await db.execute(query)
        await commit_rollback()

    @classmethod
    async def get_all(cls):
        query = select(cls.model)
        return (await db.execute(query)).scalars().all()

    @classmethod
    async def get_by_id(cls, model_id: str):
        query = select(cls.model).where(cls.model.id == model_id)
        return (await db.execute(query)).scalars()
