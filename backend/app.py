from flask import Flask, request, jsonify
from utils.add_data_in_json import add_env_config, add_customer_details
from utils.db import run_queries

app = Flask(__name__)

@app.route('/add_env', methods=['POST'])
def add_env():
    data = request.json
    env_name = data.get('env_name')
    configurations = data.get('configurations')

    if not env_name or not configurations:
        return jsonify({"error": "Missing required parameters"}), 400

    result = add_env_config(env_name, configurations)
    if "error" in result:
        return jsonify(result), 400
    return jsonify(result), 200

@app.route('/add_customer', methods=['POST'])
def add_customer():
    customer_details = request.json

    if not customer_details:
        return jsonify({"error": "Missing customer details"}), 400

    result = add_customer_details(customer_details)
    return jsonify(result), 200

@app.route('/run_query_api', methods=['POST'])
def run_query_api():
    data = request.json

    if not data:
        return jsonify({"error": "Missing data payload"}), 400
    
    env_name = data.get("env_name")
    db_name = data.get("db_name")
    flow_name = data.get("flow_name")


    if not env_name or not db_name or not flow_name:
        return jsonify({"error": "Missing reuired ddetails"}), 400
    
    try:
        run_queries(env_name,db_name,flow_name)
        return jsonify({"message":"queries executed successfully"})
    except Exception as e:
        return jsonify({"error": str(e)}), 400 

    #result = get_evidence(file_data)
    #return jsonify(result), 200

if __name__ == "__main__":
    app.run(debug=True)
    


