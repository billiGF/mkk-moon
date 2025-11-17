from src.core.db import Base
from sqlalchemy.orm import relationship
from .organization import Organization
from sqlalchemy import Table ,Column, String, ForeignKey, Numeric


class Building(Base):
    name = Column(String(50))
    address = Column(String(50))
    longitude = Column(Numeric(2, 5))
    latitude = Column(Numeric(2, 5))
    organizations = relationship(Organization, back_populates="building")