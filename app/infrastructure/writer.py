from abc import ABC, abstractmethod
from app.domain.order import Order


class OrderWriter(ABC):
    @abstractmethod
    def save(self, order: Order):
        pass