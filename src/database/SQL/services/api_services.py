from ..config.sql_database import SessionLocal
from ..repository.api_repository import execute_statement_repository
from ..schemas.facility_schema import FacilityResponse


def execute_statement_service(stmt) -> list[FacilityResponse]:
    with SessionLocal() as db:
        facilities = execute_statement_repository(db, stmt)
        facility_responses = [FacilityResponse.model_validate(f) for f in facilities]
        return facility_responses
