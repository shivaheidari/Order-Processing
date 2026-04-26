from abc import ABC, abstractmethod

class OrderWriter(ABC):
    @abstractmethod
    def save(self, order: dict):
        pass