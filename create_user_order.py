"""For this assignment, the functions in the users and items modules are not needed.
It suffices to know:
    1. each function interacts with a dependent resource (such as a database or HTTP service):
    2. get_user returns a dictionary containing a "membership" key
    3. get_item returns a dictionary containing a "price" key

If you like, you make create simple functions for these, but this is not needed.
"""

import json
from datetime import datetime
import os
from users import get_user
from items import get_item


def create_user_order(user_id: int, item_id: int) -> dict:
    """Fetch a user, fetch an item, apply a discount if the user
    is a premium member, and write the order to a file."""

    # Call user module
    user = get_user(user_id)

    # Call item module
    item = get_item(item_id)

    price = item["price"]

    if user.get("membership") == "premium":
        price *= 0.80

    order = {
        "user_id": user_id,
        "item_id": item_id,
        "final_price": round(price, 2),
        "timestamp": datetime.now().isoformat(),
    }

    # store the order
    log_path = os.path.join(os.getcwd(), "orders", f"order_{user_id}_{item_id}.json")
    with open(log_path, "w") as f:
        json.dump(order, f)

    return order