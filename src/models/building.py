from src.core.db import Base
from sqlalchemy.orm import relationship
from .organization import Organization
from sqlalchemy import Table ,Column, String, Integer, ForeignKey



class Building(Base):
    name = Column(String(50))
    address = Column(String(50))
    longitude = Column(Integer)
    latitude = Column(Integer)
    organizations = relationship(Organization, back_populates="building")