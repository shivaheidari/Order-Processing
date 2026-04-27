import json
import os
from dataclasses import asdict

from app.infrastructure.writer import OrderWriter
from app.infrastructure.path_builder import build_order_path
from app.domain.order import Order


class FileWriter(OrderWriter):
    def __init__(self, base_path: str):
        self.base_path = base_path

    def save(self, order: Order):
        log_path = build_order_path(order, self.base_path)

        try:
            os.makedirs(os.path.dirname(log_path), exist_ok=True)

        
            with open(log_path, "w") as f:
                json.dump(asdict(order), f)

        except OSError as e:
            raise RuntimeError("Failed to persist order to file system") from e