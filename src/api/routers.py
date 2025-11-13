from fastapi import APIRouter
from src.api import building_router, organization_router, activities_router



main_router = APIRouter()
main_router.include_router(building_router, tags=['Building'], prefix='/building')
main_router.include_router(organization_router, tags=['Organization'], prefix='/organization')
main_router.include_router(activities_router, tags=['Activities'], prefix='/activities')