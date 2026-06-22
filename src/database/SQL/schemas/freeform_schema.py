from pydantic import BaseModel, ConfigDict


class FreeformCreate(BaseModel):
    procedure: str
    equipment: str
    capability: str


class FreeformData(FreeformCreate):
    pass


class FreeformResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    facility_id: int
    procedure: str
    equipment: str
    capability: str
