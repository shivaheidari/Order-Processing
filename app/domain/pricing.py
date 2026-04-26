def calculate_price(base_price, membership):
    """Calculate the final price based on membership type.
    applu
    """
    if membership == 'premium':
        return round(base_price * 0.80, 2)
    return round(base_price, 2)