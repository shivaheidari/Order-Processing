import json
import os
from unittest.mock import mock_open

from app.infrastructure.file_writer import FileWriter
from app.domain.order import Order


def test_save_order(monkeypatch):
    order = Order(
        user_id=1,
        item_id=2,
        final_price=80.0,
        timestamp="2024-01-01T00:00:00",
    )

    m = mock_open()
    monkeypatch.setattr("builtins.open", m)
    monkeypatch.setattr(os, "makedirs", lambda path, exist_ok: None)

    writer = FileWriter("/fake/path")
    writer.save(order)

    m.assert_called_once()

    handle = m()
    written_data = "".join(call.args[0] for call in handle.write.call_args_list)

    parsed = json.loads(written_data)

    assert parsed["user_id"] == 1
    assert parsed["item_id"] == 2
    assert parsed["final_price"] == 80.0
    assert "timestamp" in parsed