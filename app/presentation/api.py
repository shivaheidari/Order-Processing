from flask import Flask, request, jsonify
from app.services.order_service import OrderService
from app.infrastructure.file_writer import FileWriter
from app.config import load_config

app = Flask(__name__)

def fake_user_provider():
    class Provider:
        def get_user(self, user_id):
            return {"membership": "premium"}
    return Provider()

def fake_item_provider():
    class Provider:
        def get_item(self, item_id):
            return {"price": 100}
    return Provider()

config = load_config()

service = OrderService(
    user_provider=fake_user_provider(),
    item_provider=fake_item_provider(),
    writer=FileWriter(config.base_path),
)


@app.route("/orders", methods=["POST"])
def create_order():
    user_id = request.args.get("user_id", type=int)
    item_id = request.args.get("item_id", type=int)

    if user_id is None or user_id <= 0 or item_id is None or item_id <= 0:
        return jsonify({"error": "Invalid user_id or item_id"}), 400

    try:
        order = service.create_order(user_id, item_id)
        return jsonify(order.__dict__), 200

    except ValueError as e:
        return jsonify({"error": str(e)}), 400

    except Exception as e:
        app.logger.error("Unexpected error occurred", exc_info=True)
        return jsonify({"error": "Internal server error"}), 500