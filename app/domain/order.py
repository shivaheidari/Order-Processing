from datetime import datetime
from dataclasses import dataclass

@dataclass
class Order:
    user_id : int
    item_id: int
    final_price: float
    timestamp: str


def build_order(user_id, item_id, final_price):
    return Order(
        user_id=user_id,
        item_id=item_id,
        final_price=final_price,
        timestamp=datetime.now().isoformat(),
    )