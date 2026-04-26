from unittest.mock import patch, mock_open
from legacy.create_user_order import  create_user_order


def fake_get_user(user_id):
    return {"membership": "premium"}


def fake_get_item(item_id):
    return {"price": 100}


def test_create_user_order():
    m_open = mock_open()
    
    with patch("builtins.open", m_open), patch("os.makedirs"):
        result = create_user_order(1, 1, get_user_fn=fake_get_user, get_item_fn=fake_get_item)

    m_open.return_value.write.assert_called()

    assert result["user_id"] == 1
    assert result["item_id"] == 1
    assert result["final_price"] == 80.0
    assert "timestamp" in result