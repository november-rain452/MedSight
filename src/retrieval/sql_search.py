from ..database.sql.models.model import Facility
from sqlalchemy import select
from ..database.sql.services.api_services import execute_statement_service

FIELD_MAP = {
    "organization_type": Facility.organization_type,
    "city": Facility.city,
    "country": Facility.country,
    "facility_type": Facility.facility_type,
}


def retrieve_sql(parsed_query: dict):
    stmt = select(Facility)

    for key, column in FIELD_MAP.items():
        value = parsed_query.get(key)
        if value:
            stmt = stmt.where(column == value)

    results = execute_statement_service(stmt)

    if not results:
        return []
    return results.scalars().all()
