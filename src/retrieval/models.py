from dataclasses import dataclass
from typing import Literal, Any
from src.database.sql.schemas.facility_schema import FacilityResponse


@dataclass(slots=True)
class SearchResult:
    facility_id: str
    source: Literal["sql", "vector"]
    raw_score: float
    rank: int
    content: str | None
    metadata: dict[str, Any]
    facility: FacilityResponse | None
