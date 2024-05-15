from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum


class VeichileStatus(Enum):
    AVAILABLE = 1
    BUZY = 2
    UNAVAILABLE = 0


@dataclass(frozen=True, order=True)
class VeichileModel:
    id: int
    plate: str
    status: VeichileStatus
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)
