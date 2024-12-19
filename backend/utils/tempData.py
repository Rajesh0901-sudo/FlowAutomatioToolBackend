import json
import os

def load_json(file_path):
    if not os.path.exists(file_path):
        return {}
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except Exception as e:
        print(f"An error occurred while loading {file_path}: {e}")
        return {}

def save_json(file_path, data):
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        print(f"An error occurred while saving {file_path}: {e}")

def add_env_config(env_name, configurations):
    envs_file = "./data/new_envs.json"
    envs = load_json(envs_file)
    if env_name in envs:
        return {"error": "Environment already exists"}
    envs[env_name] = configurations
    save_json(envs_file, envs)
    return {"message": "Environment added successfully"}

def add_customer_details(customer_details):
    customer_details_file = "./data/customer_details.json"
    data = load_json(customer_details_file)
    data.update(customer_details)
    save_json(customer_details_file, data)
    return {"message": "Customer details added successfully"}



from flask import Flask, request, jsonify
from utils.json_utils import add_env_config, add_customer_details

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

if __name__ == "__main__":
    app.run(debug=True)

    curl -X POST -H "Content-Type: application/json" -d '{"env_name": "illnqw8378", "configurations": {"db_user_name": "OMS1OMS", "db_password": "OMS1OMS", "db_host": "illnqw8327", "service_name": "CHRDB8378", "new_service_name": "CHRDB8378"}}' http://127.0.0.1:5000/add_env