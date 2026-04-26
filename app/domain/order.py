from datetime import datetime

def build_order(user_id, item_id, final_price):
    """
    construct the order dictionary based on
    user_id, item_id, and final_price
    """
    return {

         "user_id": user_id,
        "item_id": item_id,
        "final_price": final_price,
        "timestamp": datetime.now().isoformat(),
    }