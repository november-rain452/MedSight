from ..database.sql.models.model import Facility
from sqlalchemy import select


def retrieve_sql(parsed_query: dict):
    stmt = select(Facility)

    if parsed_query.get("organization_type"):
        stmt = stmt.where(
            Facility.organization_type == parsed_query["organization_type"]
        )
