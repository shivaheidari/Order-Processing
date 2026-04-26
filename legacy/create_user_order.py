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
from app.domain.pricing import calculate_price
from app.domain.order import build_order


def default_get_user(user_id):
    """
    Default dependency for fetching user. 
    Delayed import
    """
    from users import get_user
    return get_user(user_id)

def default_get_item(item_id):
    """
    Default dependency for fetching item. 
    Delayed import
    """
    from items import get_item
    return get_item(item_id)

def create_user_order(user_id: int, item_id: int, get_user_fn=default_get_user, get_item_fn=default_get_item) -> dict:
    """Fetch a user, fetch an item, apply a discount if the user
    is a premium member, and write the order to a file."""

    # Call user module
    user = get_user_fn(user_id)

    # Call item module
    item = get_item_fn(item_id)

    price = calculate_price(item["price"], user.get("membership"))
    
    order = build_order(user_id, item_id, price)

    # store the order
    log_path = os.path.join(os.getcwd(), "orders", f"order_{user_id}_{item_id}.json")
    with open(log_path, "w") as f:
        json.dump(order, f)

    return order