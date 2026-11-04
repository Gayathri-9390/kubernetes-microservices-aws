from flask import Flask, jsonify

app = Flask(__name__)

orders = [
    {"order_id": 101, "user_id": 1, "product_id": 1, "quantity": 1},
    {"order_id": 102, "user_id": 2, "product_id": 2, "quantity": 2}
]

@app.route("/")
def home():
    return jsonify({
        "service": "Order Service",
        "message": "Order Service is running successfully"
    })

@app.route("/orders")
def get_orders():
    return jsonify(orders)

@app.route("/health")
def health():
    return jsonify({"status": "healthy"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
