from fastapi import APIRouter, Depends
from src.core.db import async_session
from sqlalchemy.ext.asyncio import AsyncSession
from src.crud.organization import organiztaion_crud
from src.shcemas.organization import OrganizationCreate
from src.api.validators import cheking_building_exist


router = APIRouter()



@router.post('/')
async def organization(
    organization: OrganizationCreate,
    session: AsyncSession = Depends(async_session)
):
    await cheking_building_exist(
        organization.building_id, session
        )
    creating_organization = await organiztaion_crud.create(
        organization, session
        )
    return creating_organization


@router.get('/')
async def get_all_organization(
    session: AsyncSession = Depends(async_session)
):
    info = await organiztaion_crud.get(session)
    return info