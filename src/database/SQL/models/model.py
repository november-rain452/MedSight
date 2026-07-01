from sqlalchemy import Column, String, Integer, ForeignKey, JSON
from ....core.sql_database import Base
from sqlalchemy.orm import relationship


class Facility(Base):
    __tablename__ = "facilities"

    id = Column(Integer, primary_key=True, index=True)
    fid = Column(String(255), nullable=False)
    name = Column(String(255))
    specialties = Column(JSON)
    procedure = Column(JSON)
    equipment = Column(JSON)
    capability = Column(JSON)
    organization_type = Column(String(255))
    city = Column(String(255))
    country = Column(String(255))
    facility_type = Column(String(255))
