from ..schemas.facility_schema import FacilityCreate, FacilityResponse
from ..schemas.freeform_schema import FreeformCreate, FreeformResponse
from ..models.model import Facility, Freeform
from sqlalchemy.orm import Session, selectinload
from sqlalchemy import select


def insert_facility_freeform_repository(
    db: Session, freeform_data: FreeformCreate, facility_data: FacilityCreate
):
    try:
        facility = Facility(**facility_data.model_dump())
        freeform = Freeform(**freeform_data.model_dump())

        facility.freeform = freeform

        db.add(facility)
        return facility
    except Exception:
        db.rollback()
        raise


def get_facility_freeform_by_id(
    db: Session, facility_id: int
) -> FacilityResponse | None:
    stmt = (
        select(Facility)
        .options(selectinload(Facility.freeform))
        .where(Facility.id == facility_id)
    )
    result = db.execute(stmt)
    facility = result.scalar_one_or_none()

    if facility is None:
        return None

    return FacilityResponse.model_validate(facility)
