







from flask import Flask, request, jsonify, send_from_directory
from utils.add_data_in_json import DataManager
from utils.db import Database
from flask_cors import CORS, cross_origin
import os

app = Flask(__name__, static_folder='../frontend/flow_automation_front_end/build')
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

data_manager = DataManager()

@app.route('/add_env', methods=['POST'])
def add_env():
    data = request.json
    # Your existing code to handle add_env
    return jsonify({"message": "Environment added successfully"})

@app.route('/add_customer', methods=['POST'])
def add_customer():
    data = request.json
    # Your existing code to handle add_customer
    return jsonify({"message": "Customer added successfully"})

@app.route('/run_query_api', methods=['POST'])
def run_query_api():
    data = request.json
    # Your existing code to handle run_query_api
    return jsonify({"message": "Query executed successfully"})

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists(os.path.join(app.static_folder, path)):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')

if __name__ == "__main__":
    app.run(debug=True)