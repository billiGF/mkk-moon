from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base, declared_attr
from sqlalchemy import Column, Integer
from src.core.config import settings




class PREBase:
    @declared_attr
    def __tablename__(self):
        return self.__name__.lower()
    
    id = Column(Integer, primary_key=True)


Base = declarative_base(cls=PREBase)
engine = create_async_engine(settings.database_url)
AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession)


async def database():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def async_session():
    async with AsyncSessionLocal() as session:
        yield session


from typing import Annotated
from fastapi import Depends
async_session1 = Annotated[AsyncSession, Depends(async_session)]