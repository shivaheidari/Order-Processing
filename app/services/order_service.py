"""
Order Service Module.

This module provides the `OrderService` class, which orchestrates the
business logic for creating and saving user orders.
"""

from app.domain.pricing import calculate_price
from app.domain.order import build_order
from typing import Callable, Dict, Optional, Any

class OrderService:
    """
    Service class to handle operations related to user orders.

    Attributes:
        user_provider (Callable): A callable to retrieve user details by user ID.
        item_provider (Callable): A callable to retrieve item details by item ID.
        writer (Any): The order writer dependency used to save the order.
    """

    def __init__(self, user_provider, item_provider, writer):
        self.user_provider = user_provider
        self.item_provider = item_provider
        self.writer = writer

    def create_order(self, user_id: int, item_id: int) -> dict:
        user = self.user_provider.get_user(user_id)
        item = self.item_provider.get_item(item_id)

        price = calculate_price(item["price"], user.get("membership"))
        order = build_order(user_id, item_id, price)
    
        self.writer.save(order)

        return order