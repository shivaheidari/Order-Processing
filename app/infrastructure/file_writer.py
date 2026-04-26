import json
import os

def save_order(order, base_path):
    """
    store the order to filesystem as JSON file
    """
    log_path = os.path.join(
        base_path, 
        "orders",
        f"order_{order['user_id']}_{'item_id'}.json"
    )
    with open(log_path, "w") as f:
        json.dump(order, f)