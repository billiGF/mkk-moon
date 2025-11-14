from .base import CRUDBase
from src.models.activities import ActivitiesProduct, Activities
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload


class ACTIVITIESPRODUCTBase(CRUDBase):
    
    # async def get_activities_name(
    #         name: str,
    #         session: AsyncSession
    # ):

    pass

class ACTIVITIESBase(CRUDBase):
    async def get_activities_id(
            self,
            name: str,
            session: AsyncSession
    ):  
        info = await session.execute(select(Activities).options(selectinload(Activities.organization)).where(
            Activities.name == name
        ))
        result =  info.scalars().first()
        return result


activitiesproduct_crud = ACTIVITIESPRODUCTBase(ActivitiesProduct)
activities_crud = ACTIVITIESBase(Activities)