"""Database configuration"""

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from src.common.config import DSN
from src.data.models import Base


engine = create_async_engine(DSN, echo=True)
session_factory = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def drop_tables():
    """ Drop database tables """
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


async def create_tables():
    """ Create database tables """
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
