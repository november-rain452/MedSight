from ..schemas.facility_schema import FacilityCreate, FacilityResponse
from ..models.model import Facility
from sqlalchemy.orm import Session
from sqlalchemy import select
from ....utils.custom_exceptions import DuplicateFacilityError


# inserts
def insert_facility_repository(db: Session, facility_data: FacilityCreate):
    existing = db.query(Facility).filter(Facility.fid == facility_data.fid).first()

    if existing:
        raise DuplicateFacilityError("Facility already exists")

    facility = Facility(**facility_data.model_dump())

    db.add(facility)
    return facility


def insert_in_batch(db: Session, facilities: list):
    return None


# gets
def get_facility_by_id(db: Session, facility_id: int) -> FacilityResponse | None:
    stmt = select(Facility).where(Facility.id == facility_id)
    result = db.execute(stmt)
    facility = result.scalar_one_or_none()

    if facility is None:
        return None

    return FacilityResponse.model_validate(facility)
