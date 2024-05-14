from abc import ABC, abstractmethod

from delivery.domain.models import VeichileModel, VeichileStatus


class VeichileRepository(ABC):
    @abstractmethod
    def create_veichile(self, veichile: VeichileModel) -> VeichileModel:
        pass

    @abstractmethod
    def get_veichile_by_id(self, veichile_id: int) -> VeichileModel | None:
        pass

    @abstractmethod
    def update_veichile_status(
        self, veichile_id: int, status: VeichileStatus
    ) -> VeichileModel | None:
        pass
