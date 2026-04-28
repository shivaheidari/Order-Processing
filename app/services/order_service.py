"""
Order Service Module.

This module provides the `OrderService` class, which orchestrates the
business logic for creating and saving user orders.
"""

from app.domain.pricing import calculate_price
from app.domain.order import build_order, Order
from app.exceptions import ProviderDataError
from app.infrastructure.providers import UserProvider, ItemProvider
from app.infrastructure.writer import OrderWriter

class OrderService:
    """
    Service class to handle operations related to user orders.

    Attributes:
        user_provider (UserProvider): A provider to retrieve user details by user ID.
        item_provider (ItemProvider): A provider to retrieve item details by item ID.
        writer (OrderWriter): The order writer dependency used to save the order.
    """

    def __init__(
        self,
        user_provider: UserProvider,
        item_provider: ItemProvider,
        writer: OrderWriter,
    ) -> None:
        self.user_provider = user_provider
        self.item_provider = item_provider
        self.writer = writer

    def create_order(self, user_id: int, item_id: int) -> Order:
        user = self.user_provider.get_user(user_id)
        item = self.item_provider.get_item(item_id)
        
        try:
            price = calculate_price(
                item["price"],
                user.get("membership", "standard")
            )
        except (KeyError, TypeError) as e:
            raise ProviderDataError("Failed to extract expected data from providers") from e

        order = build_order(user_id, item_id, price)

        self.writer.save(order)

        return order