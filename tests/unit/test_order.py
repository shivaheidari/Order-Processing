from app.domain.order import build_order, Order

def test_build_order_structure():
    order = build_order(1, 2, 80.0)

    assert isinstance(order, Order)
    assert order.user_id == 1 
    assert order.item_id == 2
    assert order.final_price == 80.0
    assert isinstance(order.timestamp, str)