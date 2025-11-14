from pydantic import BaseModel, validator, Field
from typing import List, Union, Optional


class OrganizationBase(BaseModel):
    name: str = Field(max_length=20, min_length=5)
    phone_number: List[int]
    building_id: int

    @validator('phone_number')

    def cheking_lengh_number(value):
        for num in value:
            if len(str(num)) > 10:
                raise ValueError('Wrong Number')
            return value
            

class OrganizationCreate(OrganizationBase):
    pass


class OrganizationRM(OrganizationBase):
    id: int

    class Config:
        from_attributes=True


class OrganizationRESPONSE(BaseModel):
    id: int
    name: str
