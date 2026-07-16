from ..config.sql_database import SessionLocal
from ..repository.api_repository import execute_statement_repository
from ..schemas.facility_schema import FacilityResponse
from src.core.logger import logger


def execute_statement_service(stmt) -> list[FacilityResponse]:
    with SessionLocal() as db:
        try:
            logger.info(f"Executing sql statement: {stmt}")
            facilities = execute_statement_repository(db, stmt)
            facility_responses = [
                FacilityResponse.model_validate(f) for f in facilities
            ]
            return facility_responses
        except Exception as e:
            logger.error(f"Error executing sql statement: {stmt}")
            raise
