from sqlalchemy import Column, String, Integer, ForeignKey
from core.sql_database import Base
from sqlalchemy.orm import relationship


class Facilities(Base):
    __tablename__ = "facilities"

    id = Column(Integer, primary_key=True, index=True)
    fid = Column(String(255))
    name = Column(String(255))
    specialties = Column(String(255))
    city = Column(String(255))
    country = Column(String(255))
    facility_type = Column(String(255))

    freeform = relationship("Freeform", back_populates="facility", uselist=False)


class Freeforms(Base):
    __tablename__ = "freeforms"

    id = Column(Integer, primary_key=True)
    procedure = Column(String(255))
    equipment = Column(String(255))
    capability = Column(String(255))

    facility_id = Column(Integer, ForeignKey("facilities.id"))

    facility = relationship("Facilities", back_populates="freeform")
