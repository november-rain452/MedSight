from ..schemas.facility_schema import FacilityCreate, FacilityResponse
from ..models.model import Facility
from sqlalchemy.orm import Session
from sqlalchemy import select, insert
from src.utils.custom_exceptions import DuplicateFacilityError, EmptyBatchError


# inserts
def insert_facility_repository(db: Session, facility_data: FacilityCreate):
    existing = db.query(Facility).filter(Facility.fid == facility_data.fid).first()

    if existing:
        raise DuplicateFacilityError(
            f"Facility with fid {facility_data.fid} already exists"
        )

    facility = Facility(**facility_data.model_dump())

    db.add(facility)
    return facility


def insert_in_batch(db: Session, facilities: list[dict]):
    if not facilities:
        raise EmptyBatchError("No facilities provided for batch inserting")
    db.execute(insert(Facility), facilities)


# gets
def get_facility_by_id(db: Session, facility_id: int) -> FacilityResponse | None:
    stmt = select(Facility).where(Facility.id == facility_id)
    result = db.execute(stmt)
    facility = result.scalar_one_or_none()

    if facility is None:
        return None

    return FacilityResponse.model_validate(facility)
