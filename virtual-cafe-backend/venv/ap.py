from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allows frontend JS requests during development

@app.route("/")
def home():
    return "Flask server is running!"

@app.route("/order", methods=["POST"])
def place_order():
    data = request.json
    print("Order received:", data)
    return jsonify({"status": "success", "message": "Order placed!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)




