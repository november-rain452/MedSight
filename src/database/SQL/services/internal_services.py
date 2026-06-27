from ..schemas.facility_schema import FacilityCreate
from ....core.sql_database import SessionLocal
from ..repository.internal_repository import (
    insert_facility_repository,
    insert_in_batch,
    get_facility_by_id,
)
from ....utils.custom_exceptions import DuplicateFacilityError


# inserts
def insert_facility_service(facility_data: FacilityCreate):
    with SessionLocal() as db:
        try:
            facility = insert_facility_repository(db, facility_data)

            db.commit()
            db.refresh(facility)

            return facility
        except DuplicateFacilityError:
            raise
        except Exception:
            db.rollback()
            raise


def insert_in_batch_service(batch_sql: list[dict]):
    with SessionLocal() as db:
        return None


# gets
def get_facility_by_id_service(facility_id: int):
    with SessionLocal() as db:
        facility = get_facility_by_id(db, facility_id)
        return facility
