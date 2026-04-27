import os
from dataclasses import dataclass


@dataclass
class AppConfig:
    """Central configuration object for the application."""
    base_path: str


def load_config() -> AppConfig:
    """
    Load configuration from environment variables.
    """
    default_path = os.path.join(os.getcwd(), "orders")
    return AppConfig(
        base_path=os.getenv("ORDERS_SAVE_PATH", default_path)
    )