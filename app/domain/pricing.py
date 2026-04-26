def calculate_price(base_price, membership):
    """Calculate the final price based on membership type.
    Applies a discount for premium users.
    """
    if membership == 'premium':
        return round(base_price * 0.80, 2)
    return round(base_price, 2)