from src.core.db import Base
from sqlalchemy import Column, Integer, String, ForeignKey, JSON
from sqlalchemy.orm import relationship

class Organization(Base):
    name = Column(String, unique=True)
    phone_number = Column(JSON, default=[])
    building_id = Column(Integer, ForeignKey('building.id'), nullable=False)

    building = relationship("Building", back_populates="organizations")
