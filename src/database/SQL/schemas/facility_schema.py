from pydantic import BaseModel, ConfigDict
from .freeform_schema import FreeformResponse


class FacilityCreate(BaseModel):
    fid: str
    name: str
    specialties: list[str]
    city: str
    country: str
    facility_type: str


class FacilityResponse(BaseModel):

    model_config = ConfigDict(from_attributes=True)

    name: str
    specialties: list[str]
    city: str
    country: str
    facility_type: str
    freeform: FreeformResponse | None = None
