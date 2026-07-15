from ..schemas.facility_schema import FacilityCreate, FacilityResponse
from ..config.sql_database import SessionLocal
from ..repository.internal_repository import (
    insert_facility_repository,
    insert_in_batch,
    get_facility_by_id,
)
from src.utils.custom_exceptions import DuplicateFacilityError
from src.core.logger import logger


# inserts
def insert_facility_service(facility_data: FacilityCreate) -> FacilityResponse:
    logger.info(f"Attempting to insert facility: {facility_data.fid}")
    with SessionLocal() as db:
        try:
            facility = insert_facility_repository(db, facility_data)

            db.commit()
            db.refresh(facility)
            logger.info(f"Facility inserted successfully with ID: {facility.id}")

            return FacilityResponse.model_validate(facility)
        except DuplicateFacilityError as e:
            logger.warning(f"Duplicate facility detected: {facility_data.name}. {e}")
            raise
        except Exception as e:
            logger.error(f"Facility insertion failed: {e}", exc_info=True)
            db.rollback()
            raise


def insert_in_batch_service(batch_sql: list[dict]) -> None:

    validated = [FacilityCreate.model_validate(row).model_dump() for row in batch_sql]
    logger.info(f"Starting batch insertion of {len(validated)} facilities")
    with SessionLocal() as db:
        try:
            insert_in_batch(db, validated)
            db.commit()
            logger.info(
                f"Batch seeding successful. {len(validated)} facilities inserted."
            )
        except Exception as e:
            logger.error(f"Batch seeding failed: {e}", exc_info=True)
            db.rollback()
            raise


# gets
def get_facility_by_id_service(facility_id: int) -> FacilityResponse | None:
    logger.info(f"Retrieving facility by ID: {facility_id}")
    with SessionLocal() as db:
        try:
            facility = get_facility_by_id(db, facility_id)
            if facility is None:
                logger.warning(f"Facility with facility id: {facility_id} not found")
                return None

            return FacilityResponse.model_validate(facility)
        except Exception as e:
            logger.error(
                f"Error retrieving facility ID {facility_id}: {e}", exc_info=True
            )
            raise
