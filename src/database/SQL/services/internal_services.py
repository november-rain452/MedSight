from ..schemas.facility_schema import FacilityCreate
from ..config.sql_database import SessionLocal
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

    validated = [FacilityCreate.model_validate(row).model_dump() for row in batch_sql]
    with SessionLocal() as db:
        try:
            insert_in_batch(db, validated)
            db.commit()
        except Exception:
            db.rollback()
            raise


# gets
def get_facility_by_id_service(facility_id: int):
    with SessionLocal() as db:
        facility = get_facility_by_id(db, facility_id)
        return facility
