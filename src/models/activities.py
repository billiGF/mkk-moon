from sqlalchemy import Column, String, ForeignKey, Integer, Table
from sqlalchemy.orm import relationship
from src.core.db import Base



organization_activities = Table(
    "organization_activities",
    Base.metadata,
    Column("organization_id", Integer, ForeignKey("organization.id")),
    Column("activitiesproduct_id", Integer, ForeignKey("activitiesproduct.id"))
)


class ActivitiesProduct(Base):
    name = Column(String)
    activities_id = Column(Integer, ForeignKey("activities.id"))
    organization = relationship("Organization", secondary=organization_activities, back_populates="activitiesproduct")


class Activities(Base):
    name = Column(String, unique=True)
    activities_product = relationship(ActivitiesProduct, cascade="delete")


