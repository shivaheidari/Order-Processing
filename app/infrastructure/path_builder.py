import os
from app.domain.order import Order


def build_order_path(order: Order, base_path: str) -> str:
    """
    Build filesystem path for order persistence.
    """
    return os.path.join(
        base_path,
        f"order_{order.user_id}_{order.item_id}.json"
    )