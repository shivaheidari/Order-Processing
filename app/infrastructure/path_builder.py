import os

def build_order_path(order: dict, base_path: str) -> str:
    return os.path.join(
        base_path,
        "orders",
        f"order_{order['user_id']}_{order['item_id']}.json"
    )