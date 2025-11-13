from .base import CRUDBase
from sqlalchemy import select
from src.models.building import Building
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload



class BUILDINGCrud(CRUDBase):
    
    
    async def get_building_by_id(
            self,
            building_id,
            session: AsyncSession
        ):
        result =  await session.execute(
            select(Building)
            .options(selectinload(Building.organizations))
            .where(Building.id == building_id)
        )
        result = result.scalars().first()
        return result
    

    async def get_building_by_name(
            self,
            building_name,
            session: AsyncSession,
    ):
        result = await session.execute(
            select(Building)
            .where(Building.name == building_name)
        )
        result = result.scalars().first()
        return result



building_crud = BUILDINGCrud(Building)