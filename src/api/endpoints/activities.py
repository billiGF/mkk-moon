from fastapi import APIRouter
from src.core.db import async_session1
from src.crud.activities import activities_crud

router = APIRouter()



@router.get('/')
async def get_activities_product(
    session: async_session1
):
    info = await activities_crud.get_multi(session)
    return info



@router.get('/{name}')
async def get_organization_activity_by_name(
    name: str,
    session: async_session1
):
    info = await activities_crud.get_activities_id(name, session)
    return info