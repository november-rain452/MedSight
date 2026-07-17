from pydantic import BaseModel, ConfigDict


class FacilityCreate(BaseModel):
    fid: str
    name: str
    specialties: list[str]
    procedure: list[str]
    equipment: list[str]
    capability: list[str]
    organization_type: str | None = None
    city: str | None = None
    country: str | None = None
    facility_type: str | None = None


class FacilityResponse(BaseModel):

    model_config = ConfigDict(from_attributes=True)

    id: int
    fid: str
    name: str
    specialties: list[str] | None
    procedure: list[str] | None
    equipment: list[str] | None
    capability: list[str] | None
    organization_type: str | None = None
    city: str | None = None
    country: str | None = None
    facility_type: str | None = None
