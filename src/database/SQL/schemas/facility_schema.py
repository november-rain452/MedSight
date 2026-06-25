from pydantic import BaseModel, ConfigDict
from .freeform_schema import FreeformResponse


class FacilityCreate(BaseModel):
    fid: str
    name: str
    specialties: list[str]
    organization_type: str | None = None
    city: str | None = None
    country: str | None = None
    facility_type: str | None = None


class FacilityResponse(BaseModel):

    model_config = ConfigDict(from_attributes=True)

    name: str
    specialties: list[str]
    organization_type: str | None = None
    city: str | None = None
    country: str | None = None
    facility_type: str | None = None
    freeform: FreeformResponse | None = None
