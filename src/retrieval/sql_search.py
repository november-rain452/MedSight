from ..database.sql.models.model import Facility
from sqlalchemy import select, func, or_
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

    if "specialties" in parsed_query:
        stmt = apply_specialty_filter(stmt, parsed_query["specialties"])
    if "procedures" in parsed_query:
        stmt = apply_procedure_filter(stmt, parsed_query["procedures"])
    if "equipments" in parsed_query:
        stmt = apply_equipment_filter(stmt, parsed_query["equipments"])

    results = execute_statement_service(stmt)

    return results.scalars().all() if results is not None else []


def apply_specialty_filter(stmt, specialties):
    if not specialties:
        return stmt

    conditions = []

    for specialty in specialties:
        conditions.append(Facility.specialties.contains([specialty]))

    return stmt.where(or_(*conditions))


def apply_procedure_filter(stmt, procedures):
    if not procedures:
        return stmt

    conditions = []

    for procedure in procedures:
        conditions.append(Facility.procedure.contains([procedure]))

    return stmt.where(or_(*conditions))


def apply_equipment_filter(stmt, equipments):
    if not equipments:
        return stmt

    conditions = []

    for equipment in equipments:
        conditions.append(Facility.equipment.contains([equipment]))

    return stmt.where(or_(*conditions))
