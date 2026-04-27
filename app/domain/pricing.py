def calculate_price(base_price, membership):
    if membership == 'premium':
        return round(base_price * 0.80, 2)

    return round(base_price, 2)