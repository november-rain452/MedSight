from pydantic import BaseModel, ConfigDict


class FreeformCreate(BaseModel):
    procedure: list[str]
    equipment: list[str]
    capability: list[str]


class FreeformData(FreeformCreate):
    pass


class FreeformResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    facility_id: int
    procedure: list[str]
    equipment: list[str]
    capability: list[str]
