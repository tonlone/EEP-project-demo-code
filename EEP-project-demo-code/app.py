from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/check', methods=['POST'])
def check_payment():
    data = request.json
    if random.random() > 0.5:
        return jsonify({"status": "success", "message": "Payment check successful"})
    else:
        return jsonify({"status": "error", "message": "Error: [Country not authorized, Currency does not allow, Amount is exceeding limit ...]"})

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=8080)