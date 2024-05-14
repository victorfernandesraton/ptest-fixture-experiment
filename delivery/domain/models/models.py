from dataclasses import dataclass
from datetime import datetime
from enum import Enum


class VeichileStatus(Enum):
    AVALIABLE = 1
    BUZY = 2
    UNAVALIABLE = 0


@dataclass(frozen=True, order=True)
class VeichileModel:
    id: int
    plate: str
    status: VeichileStatus
    created_at: datetime
    updated_at: datetime
