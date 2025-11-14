from fastapi import APIRouter, Depends
from src.shcemas.building import BuildingCreate, BuildingResponse, BuildingRM, BuildingUpdate
from src.core.db import async_session, async_session1
from sqlalchemy.ext.asyncio import AsyncSession
from src.crud.building import building_crud
from src.api.validators import cheking_building_exist, cheking_building_name_exist



router = APIRouter()



@router.post('/')
async def create_building(
    building_form: BuildingCreate,
    session: async_session1
):
   info = await building_crud.create(
      building_form, session
   )
   return info


@router.get('/{name}')
async def get_building_by_name(
   building_name,
   session: async_session1,
):
   info = await cheking_building_name_exist(
      building_name, session
   )
   return info


@router.get('/', response_model=list[BuildingResponse])
async def get_all_building(
   session: AsyncSession = Depends(async_session)
):
   info = await building_crud.get_multi(session)
   return info


@router.get('/{name}/')
async def get_all_organization_on_building(
   building_name: str,
   session: AsyncSession = Depends(async_session)
):
   info = await cheking_building_name_exist(
      building_name, session
   )
   return info


@router.patch('/', response_model=BuildingRM)
async def updating_building(
   building_id: int,
   building: BuildingUpdate,
   session: AsyncSession = Depends(async_session),
):
   object = await cheking_building_exist(
      building_id, session
   )
   info = await building_crud.update(
      db_obj=object, building=building, session=session
   )
   return info 