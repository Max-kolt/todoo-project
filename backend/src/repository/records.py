from sqlalchemy.future import select
from sqlalchemy import update
from .base_repo import BaseRepo
from src.models.records import Record
from config import db, commit_rollback


class RecordRepository(BaseRepo):
    model = Record

    @staticmethod
    async def get_by_user_id(user_id: str):
        query = select(Record).where(Record.user_id == user_id)
        return (await db.execute(query)).scalars().all()

    @staticmethod
    async def get_archived(user_id: str):
        query = select(Record).where(Record.user_id == user_id and Record.archive == True)
        return (await db.execute(query)).scalars().all()

    @staticmethod
    async def get_unarchived(user_id: str):
        query = select(Record).where(Record.user_id == user_id and Record.archive == False)
        return (await db.execute(query)).scalars().all()

    @staticmethod
    async def update_complited(record_id: str):
        query = update(Record)\
            .where(Record.id==record_id)\
            .values(archive=True, complited=True)\
            .execution_options(synchronize_session='fetch')
        await db.execute(query)
        await commit_rollback()