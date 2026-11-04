from flask import Flask, jsonify

app = Flask(__name__)

users = [
    {"id": 1, "name": "Gayathri", "role": "Admin"},
    {"id": 2, "name": "Rahul", "role": "Customer"}
]

@app.route("/")
def home():
    return jsonify({
        "service": "User Service",
        "message": "User Service is running successfully"
    })

@app.route("/users")
def get_users():
    return jsonify(users)

@app.route("/health")
def health():
    return jsonify({"status": "healthy"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
