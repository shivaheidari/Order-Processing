from abc import ABC, abstractmethod
from typing import Dict, Any


class UserProvider(ABC):
    @abstractmethod
    def get_user(self, user_id: int) -> Dict[str, Any]:
        pass


class ItemProvider(ABC):
    @abstractmethod
    def get_item(self, item_id: int) -> Dict[str, Any]:
        pass