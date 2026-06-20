from ..schemas.facility_schema import FacilityCreate
from ..schemas.freeform_schema import FreeformCreate
from ..models.model import Facility, Freeform
from sqlalchemy.orm import Session


def insert_facility_freeform_repository(
    db: Session, freeform_data: FreeformCreate, facility_data: FacilityCreate
):
    facility = Facility(**facility_data.model_dump())
    freeform = Freeform(**freeform_data.model_dump())

    facility.freeform = freeform

    db.add(facility)
    return facility
