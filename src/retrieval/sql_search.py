from ..database.sql.models.model import Facility
from sqlalchemy import select, or_, func
from ..database.sql.services.api_services import execute_statement_service
from .models import FacilityResult
from ..database.sql.schemas.facility_schema import FacilityResponse

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

    if parsed_query.get("specialties"):
        stmt = apply_specialty_filter(stmt, parsed_query["specialties"])
    if parsed_query.get("procedures"):
        stmt = apply_procedure_filter(stmt, parsed_query["procedures"])
    if parsed_query.get("equipments"):
        stmt = apply_equipment_filter(stmt, parsed_query["equipments"])
    if parsed_query.get("capabilities"):
        stmt = apply_capability_filter(stmt, parsed_query["capabilities"])

    results = execute_statement_service(stmt)
    pyd_results = [
        FacilityResult(
            facility_id=res.fid,
            facility=FacilityResponse.model_validate(res),
            metadata={"source": "sql"},
        )
        for res in results.scalars().all()
        if res is not None
    ]
    return pyd_results


def apply_specialty_filter(stmt, specialties):
    if not specialties:
        return stmt
    conditions = []
    for specialty in specialties:
        conditions.append(
            func.json_contains(Facility.specialties, func.json_quote(specialty))
        )
    return stmt.where(or_(*conditions))


def apply_procedure_filter(stmt, procedures):
    if not procedures:
        return stmt
    conditions = []
    for procedure in procedures:
        conditions.append(
            func.json_contains(Facility.procedure, func.json_quote(procedure))
        )
    return stmt.where(or_(*conditions))


def apply_equipment_filter(stmt, equipments):
    if not equipments:
        return stmt
    conditions = []
    for equipment in equipments:
        conditions.append(
            func.json_contains(Facility.equipment, func.json_quote(equipment))
        )
    return stmt.where(or_(*conditions))


def apply_capability_filter(stmt, capabilities):
    if not capabilities:
        return stmt
    conditions = []
    for capability in capabilities:
        conditions.append(
            func.json_contains(Facility.capability, func.json_quote(capability))
        )
    return stmt.where(or_(*conditions))
