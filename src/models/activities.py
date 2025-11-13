from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship
from src.core.db import Base



class ActivitiesProduct(Base):
    name = Column(String)
    activities_id = Column(Integer, ForeignKey('activities.id'), unique=True)


class Activities(Base):
    name = Column(String, unique=True)
    activities_product = relationship(ActivitiesProduct, cascade='delete')


