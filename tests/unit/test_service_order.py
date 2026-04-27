from app.services.order_service import OrderService


class FakeUserProvider:
    def get_user(self, user_id):
        return {"membership": "premium"}


class FakeItemProvider:
    def get_item(self, item_id):
        return {"price": 100}


class FakeWriter:
    def __init__(self):
        self.saved = None

    def save(self, order):
        self.saved = order


def test_create_order():
    user_provider = FakeUserProvider()
    item_provider = FakeItemProvider()
    writer = FakeWriter()

    service = OrderService(user_provider, item_provider, writer)

    result = service.create_order(1, 1)

    assert result.user_id == 1
    assert result.item_id == 1
    assert result.final_price == 80.0
    assert isinstance(result.timestamp, str)

    assert writer.saved == result