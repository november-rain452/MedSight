from ..schemas.facility_schema import FacilityCreate
from ..schemas.freeform_schema import FreeformCreate
from ....core.sql_database import SessionLocal
from ..repository.internal_repository import insert_facility_freeform_repository


def insert_facility_freeform_service(
    freeform_data: FreeformCreate, facility_data: FacilityCreate
):
    with SessionLocal() as db:
        facility = insert_facility_freeform_repository(db, freeform_data, facility_data)
        db.commit()
        db.refresh(facility)
        db.refresh(facility.freeform)
        return facility
