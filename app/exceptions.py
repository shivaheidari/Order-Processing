class OrderProcessingError(Exception):
    """Base exception for all order processing errors."""
    pass


class OrderPersistenceError(OrderProcessingError):
    """Raised when an order cannot be saved to the underlying storage."""
    pass


class ProviderDataError(OrderProcessingError):
    """Raised when upstream providers return missing or invalid data."""
    pass