from ..schemas.facility_schema import FacilityCreate, FacilityResponse
from ..schemas.freeform_schema import FreeformCreate, FreeformData
from ..models.model import Facility, Freeform
from sqlalchemy.orm import Session, selectinload
from sqlalchemy import select


def insert_facility_freeform_repository(
    db: Session, freeform_data: FreeformCreate, facility_data: FacilityCreate
):
    existing = db.query(Facility).filter(Facility.fid == facility_data.fid).first()

    if existing:
        raise Exception("Facility already exists")

    try:
        facility = Facility(**facility_data.model_dump())
        freeform = Freeform(**freeform_data.model_dump())

        facility.freeform = freeform

        db.add(facility)
        return facility
    except Exception:
        db.rollback()
        raise


def update_or_insert_freeform(
    db: Session, facility_id: int, freeform_data: FreeformData
):
    facility = db.query(Facility).filter(facility_id == Facility.id).first()

    if not facility:
        raise Exception("Facility not found")

    if facility.freeform:
        facility.freeform.procedure = freeform_data.procedure
        facility.freeform.capability = freeform_data.capability
        facility.freeform.equipment = freeform_data.equipment
    else:
        facility.freeform = Freeform(**freeform_data.model_dump())

    return facility


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
