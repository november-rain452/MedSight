from ..schemas.facility_schema import FacilityCreate
from ..schemas.freeform_schema import FreeformCreate, FreeformData
from ....core.sql_database import SessionLocal
from ..repository.internal_repository import (
    insert_facility_freeform_repository,
    get_facility_freeform_by_id,
    update_or_insert_freeform,
)


def insert_facility_freeform_service(
    freeform_data: FreeformCreate, facility_data: FacilityCreate
):
    with SessionLocal() as db:

        facility = insert_facility_freeform_repository(db, freeform_data, facility_data)

        db.commit()
        db.refresh(facility)
        db.refresh(facility.freeform)

        return facility


def update_or_insert_freeform_service(facility_id: int, freeform_data: FreeformData):

    with SessionLocal() as db:

        facility = update_or_insert_freeform(db, facility_id, freeform_data)
        db.commit()
        db.refresh(facility)

        return facility


def get_facility_freeform_by_id_service(facility_id: int):
    with SessionLocal() as db:
        facility = get_facility_freeform_by_id(db, facility_id)
        return facility
