from .base import CRUDBase
from src.models.organization import Organization


class ORGANIZATIONCrud(CRUDBase):
    pass


organiztaion_crud = ORGANIZATIONCrud(Organization)