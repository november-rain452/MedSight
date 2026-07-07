from dataclasses import dataclass, field
from typing import Literal, Any
from src.database.sql.schemas.facility_schema import FacilityResponse


@dataclass(slots=True)
class SearchResult:
    facility_id: str
    source: Literal["sql", "vector"]
    score: float
    rank: int
    content: str | None
    metadata: dict[str, Any]
    facility: FacilityResponse | None


@dataclass(slots=True)
class FacilityResult:
    facility_id: str
    facility: FacilityResponse
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass(slots=True)
class VectorResult:
    facility_id: str
    content: str | None
    metadata: dict[str, Any]
    distance: float
