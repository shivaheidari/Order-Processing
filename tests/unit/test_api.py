from app.presentation.api import app


def test_create_order_success():
    client = app.test_client()

    response = client.post("/orders?user_id=1&item_id=1")

    assert response.status_code == 200

    data = response.get_json()
    assert data["user_id"] == 1
    assert data["item_id"] == 1
    assert data["final_price"] == 80.0
    assert "timestamp" in data


def test_create_order_invalid():
    client = app.test_client()

    response = client.post("/orders?user_id=-1&item_id=1")

    assert response.status_code == 400