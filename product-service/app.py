from flask import Flask, jsonify

app = Flask(__name__)

products = [
    {"id": 1, "name": "Laptop", "price": 55000},
    {"id": 2, "name": "Mobile", "price": 25000},
    {"id": 3, "name": "Headphones", "price": 2000}
]

@app.route("/")
def home():
    return jsonify({
        "service": "Product Service",
        "message": "Product Service is running successfully"
    })

@app.route("/products")
def get_products():
    return jsonify(products)

@app.route("/health")
def health():
    return jsonify({"status": "healthy"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
