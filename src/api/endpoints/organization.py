from fastapi import APIRouter, Depends
from src.core.db import async_session, async_session1
from sqlalchemy.ext.asyncio import AsyncSession
from src.crud.organization import organiztaion_crud
from src.shcemas.organization import OrganizationCreate, OrganizationRESPONSE
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


@router.get('/', response_model=list[OrganizationRESPONSE])
async def get_all_organization(
    session: AsyncSession = Depends(async_session)
):
    info = await organiztaion_crud.get_multi(session)
    return info


@router.get('/{id}')
async def get_organization_by_id(
    id: int,
    session: async_session1
):
    info = await organiztaion_crud.get(
        id, session
    )
    return info