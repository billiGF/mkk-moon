from typing import Optional
from pydantic import BaseModel, validator



class BuildingBase(BaseModel):
    name: str
    address: str
    longitude: float
    latitude: float

    @validator('address')
    def validating_address(value):
        if "г" not in value.split() or 'у' not in value.split():
            raise ValueError("Перед городом и улицы должны стоять два значение: г-город у-улица  ")
        return value
    
class BuildingCreate(BuildingBase):
    pass


class BuildingUpdate(BuildingBase):
    name: Optional[str] = None
    address: Optional[str] = None
    longitude: Optional[float] = None
    latitude: Optional[float] = None


class BuildingResponse(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes=True


class BuildingRM(BuildingBase):
    id: int

    class Config:
        from_attributes=True