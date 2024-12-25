# app.py
from flask import Flask, request, jsonify
from utils.add_data_in_json import DataManager
from utils.db import Database
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

data_manager = DataManager()

@app.route('/add_env', methods=['POST'])
def add_env():

    data = request.json

    print(data)

    env_name = data.get('env_name')
    configurations = data.get('configurations')

    if not env_name or not configurations:
        print("missing data in add env")
        return jsonify({"error": "Missing required parameters"}), 400
    

    result = data_manager.add_env_config(env_name, configurations)

    print(result)

    if "error" in result:
        return jsonify(result), 200
    return jsonify(result), 200

@app.route('/add_customer', methods=['POST'])
def add_customer():
    customer_details = request.json

    if not customer_details:
        return jsonify({"error": "Missing customer details"}), 400

    result = data_manager.add_customer_details(customer_details)
    return jsonify(result), 200

@app.route('/run_query_api', methods=['POST'])
def run_query_api():
    data = request.json

    print(data)

    if not data:
        return jsonify({"error": "Missing data payload"}), 400
    
    env_name = data.get("env_name")
    db_name = data.get("db_name")
    flow_name = data.get("flow_name")


    if not env_name or not db_name or not flow_name:
        return jsonify({"error": "Missing required details"}), 400

    try:
        db = Database(env_name)
        db.run_queries(db_name, flow_name)
        return jsonify({"message": "queries executed successfully"})
    except Exception as e:
        return jsonify({"error": str(e)}), 400 

if __name__ == "__main__":
    app.run(debug=True)