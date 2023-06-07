# noinspection PyInterpreter
from sqlmodel import SQLModel
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

SQLALCHEMY_URL = "postgresql+asyncpg://test_user:qwerty@localhost:5432/test_db"


SECRET_KEY = "AsDFghJKLasdFGHJklasDFGHJklasdFGHJKL"
ALGORITHM = "HS256"


class AsyncDbSession():
    def __init__(self) -> None:
        self.session = None
        self.engine = None
        self.base = None

    def __getattr__(self, name):
        return getattr(self.session, name)

    def init(self):
        self.engine = create_async_engine(SQLALCHEMY_URL, future=True, echo=True)
        self.session = sessionmaker(self.engine, expire_on_commit=False, class_=AsyncSession)()

    async def create_all(self):
        async with self.engine.begin() as conn:
            await conn.run_sync(SQLModel.metadata.create_all)


db = AsyncDbSession()


async def commit_rollback():
    try:
        await db.commit()
    except Exception:
        await db.rollback()
        raise
