from ..database.sql.models.model import Facility
from sqlalchemy import select
from ..database.sql.services.api_services import execute_statement_service


def retrieve_sql(parsed_query: dict):
    stmt = select(Facility)

    if parsed_query.get("organization_type"):
        stmt = stmt.where(
            Facility.organization_type == parsed_query["organization_type"]
        )

    if parsed_query.get("city"):
        stmt = stmt.where(Facility.city == parsed_query["city"])

    if parsed_query.get("country"):
        stmt = stmt.where(Facility.country == parsed_query["country"])

    if parsed_query.get("facility_type"):
        stmt = stmt.where(Facility.facility_type == parsed_query["facility_type"])

    results = execute_statement_service(stmt)

    if not results:
        return []
    return results.scalars().all()
