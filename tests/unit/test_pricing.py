from app.domain.pricing import calculate_price


def test_calculate_price_premuim():
    assert calculate_price(100, "premium") == 80.0


def test_calculate_price_regular():
    assert calculate_price(100, "regular") == 100