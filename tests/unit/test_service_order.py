from app.services.order_service import OrderService


def fake_user(user_id):
    return {"membership": "premium"}


def fake_item(item_id):
    return {"price": 100}


class FakeWriter:
    def __init__(self):
        self.saved = None

    def save(self, order):
        self.saved = order


def test_create_order():
    writer = FakeWriter()

    service = OrderService(fake_user, fake_item, writer)

    result = service.create_order(1, 1)

    assert result["user_id"] == 1
    assert result["item_id"] == 1
    assert result["final_price"] == 80.0
    assert "timestamp" in result

    assert writer.saved == result