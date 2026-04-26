import json
from unittest.mock import mock_open

from app.infrastructure.file_writer import save_order


def test_save_order(monkeypatch):
    order = {
        "user_id": 1,
        "item_id": 2,
        "final_price": 80.0,
    }

    m = mock_open()
    monkeypatch.setattr("builtins.open", m)

    save_order(order, "/fake/path")

    m.assert_called_once()

    handle = m()
    written_data = "".join(call.args[0] for call in handle.write.call_args_list)

    parsed = json.loads(written_data)

    assert parsed["user_id"] == 1
    assert parsed["item_id"] == 2
    assert parsed["final_price"] == 80.0