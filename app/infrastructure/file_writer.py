import json
import os
from app.infrastructure.writer import OrderWriter
from app.infrastructure.path_builder import build_order_path

class FileWriter(OrderWriter):
    def __init__(self, base_path: str):
        self.base_path = base_path

    def save(self, order: dict):
        log_path = build_order_path(order, self.base_path)
        
        os.makedirs(os.path.dirname(log_path), exist_ok=True)
        with open(log_path, "w") as f:
            json.dump(order, f)