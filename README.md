# Order Processing System

This project refactors the create_user_order function to improve
testability, modularity, and separation of concerns.

## Architecture

layered architecture (closed) has been used for seperation of concerns and modulariy, and testblity:

- **Domain Layer (`app/domain/`)**: Contains the core business logic and data models (e.g., the `Order` dataclass, pricing and discount calculation). 
- **Service Layer (`app/services/`)**: Orchestrates business use cases (e.g., `OrderService`). It retrieves data from providers, applies domain logic, and delegates persistence to the infrastructure layer.
- **Infrastructure Layer (`app/infrastructure/`)**: Handles I/O operations and external concerns, such as writing order files to the filesystem (`FileWriter`) and retrieving data (`Providers`).
- **Presentation Layer (`app/presentation/`)**: Exposes the application to the outside world via a Flask REST API (`api.py`).

## Prerequisites

- Python 3.10+
- `pip` (Python package installer)

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd Order-Processing
   ```

2. Create and activate a virtual environment (optional but recommended):
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

The application is configured using environment variables. You can create a `.env` file in the root directory to set these variables.

**Example `.env`:**
```env
ORDERS_SAVE_PATH=/var/log/my_app/orders
```

If `ORDERS_SAVE_PATH` is not set, orders will default to being saved in an `orders/` directory within the current working directory.

## Running the Application

The project provides a Flask API to interact with the service. To start the server:

```bash
export FLASK_APP=app/presentation/api.py
flask run
```

### API Endpoints

- **POST `/orders?user_id=<user_id>&item_id=<item_id>`**
  Creates a new order for a user and an item, applies any applicable discounts, and persists the order to the filesystem as JSON.

## Running Tests

The project has a robust suite of unit tests built with `pytest`. To run the test suite and ensure everything is working correctly:

```bash
pytest tests/
```
