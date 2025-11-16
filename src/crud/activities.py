from .base import CRUDBase
from src.models.activities import ActivitiesProduct, Activities
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload



class ACTIVITIESPRODUCTBase(CRUDBase):
        pass

    

class ACTIVITIESBase(CRUDBase):
    async def get_activities_id(
            self,
            name: str,
            session: AsyncSession
    ):  
        info = await session.execute(select(ActivitiesProduct).options(selectinload(ActivitiesProduct.organization)).where(
            ActivitiesProduct.name == name
        ))
        result =  info.scalars().first()
        return result


activitiesproduct_crud = ACTIVITIESPRODUCTBase(ActivitiesProduct)
activities_crud = ACTIVITIESBase(Activities)