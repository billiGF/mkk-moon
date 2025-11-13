from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from fastapi.encoders import jsonable_encoder


class CRUDBase:
    def __init__(self, model):
        self.model = model


    async def create(
            self,
            creating_form,
            session: AsyncSession
        ):
        building = creating_form.dict()
        info = self.model(**building)
        session.add(info)
        await session.commit()
        await session.refresh(info)
        return info 
    

    async def get(
            self,
            session: AsyncSession,            
        ):
        info = await session.execute(select(self.model))
        info = info.scalars().all()
        return info
    
    
    async def update(
            self,
            db_obj,
            building,
            session: AsyncSession,
    ):
        obj_data = jsonable_encoder(db_obj)
        update_data = building.dict(exclude_unset=True)

        for field in obj_data:
            if field in update_data:
                setattr(db_obj, field, update_data[field])
        session.add(db_obj)
        await session.commit()
        await session.refresh(db_obj)
        return db_obj