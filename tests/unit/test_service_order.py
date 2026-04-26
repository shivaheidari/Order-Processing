"""Unit tests for the OrderService class."""

from app.services.order_service import OrderService

def fake_user(user_id):
    return {"membership": "premium"}

def fake_item(item_id):
    return {"price": 100}

def test_create_order(monkeypatch):
    """Test creating an order applies the correct discount and saves the order."""
    # Arrange
    service = OrderService(fake_user, fake_item)

    calls = {}

    def fake_save(order, path):
        calls["order"] = order
        calls["path"] = path

    # Mock infrastructure
    monkeypatch.setattr(
        "app.services.order_service.save_order",
        fake_save
    )

    # Act
    result = service.create_order(1, 1)

    # Assert
    assert result["user_id"] == 1
    assert result["item_id"] == 1
    assert result["final_price"] == 80.0
    assert "timestamp" in result

    assert calls["order"] == result