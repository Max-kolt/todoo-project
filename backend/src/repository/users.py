from sqlalchemy import select
from sqlalchemy import update

from .base_repo import BaseRepo
from src.models.users import User
from config import db, commit_rollback


class UserRepository(BaseRepo):
    model = User

    @staticmethod
    async def get_by_username(username: str):
        query = select(User.password, User.username, User.lname, User.fname).where(User.username == username)
        return (await db.execute(query)).scalar_one_or_none()

    @staticmethod
    async def update_password(username: str, new_password: str):
        query = update(User)\
            .where(User.username == username)\
            .values(password=new_password)\
            .execution_options(synchronize_session='fetch')
        await db.execute(query)
        await commit_rollback()