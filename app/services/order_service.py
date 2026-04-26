"""
Order Service Module.

This module provides the `OrderService` class, which orchestrates the
business logic for creating and saving user orders.
"""

from app.domain.pricing import calculate_price
from app.domain.order import build_order
from app.infrastructure.file_writer import save_order
from typing import Callable, Dict, Optional, Any
import os

class OrderService:
    """
    Service class to handle operations related to user orders.

    Attributes:
        user_provider (Callable): A callable to retrieve user details by user ID.
        item_provider (Callable): A callable to retrieve item details by item ID.
        base_path (str): The base directory path where order files will be saved.
    """

    def __init__(
        self, 
        user_provider: Callable[[int], Dict[str, Any]], 
        item_provider: Callable[[int], Dict[str, Any]], 
        base_path: Optional[str] = None
    ):
        self.user_provider = user_provider
        self.item_provider = item_provider
        self.base_path = base_path or os.getcwd()

    def create_order(self, user_id: int, item_id: int) -> dict:
        user = self.user_provider(user_id)
        item = self.item_provider(item_id)

        price = calculate_price(item["price"], user.get("membership"))
        order = build_order(user_id, item_id, price)

        save_order(order, self.base_path)

        return order