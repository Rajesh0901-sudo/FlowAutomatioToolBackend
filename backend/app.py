# app.py
from flask import Flask, request, jsonify,send_from_directory
from .utils.add_data_in_json import DataManager
from .utils.db import Database
from flask_cors import CORS, cross_origin
from .utils.handle_external_api import handle_external_api_method
import os
import webbrowser
import threading

app = Flask(__name__, static_folder='../frontendNew/flow_automation_front_end/build')
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
    document_path = data.get("document_path")
    document_name =  data.get("document_name")
    is_to_save_data_in_csv =  data.get("toTakeCsv")


    if not env_name or not db_name or not flow_name:
        return jsonify({"error": "Missing required details"}), 400

    try:
        db = Database(env_name)
        db.run_queries(db_name, flow_name,document_path,document_name,is_to_save_data_in_csv)
        return jsonify({"message": "queries executed successfully"})
    except Exception as e:
        return jsonify({"error": str(e)}), 400 


@app.route('/run_query_external_api', methods=['POST'])
def run_query_external_api():
    data = request.json

    #print(data)

    if not data:
        return jsonify({"error": "Missing data payload"}), 400
    
    query_response = handle_external_api_method(data)

    return jsonify({"message": "queries executed successfully"})

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    print("here",path)
    if path != "" and os.path.exists(os.path.join(app.static_folder, path)):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')

def open_browser():
    webbrowser.open_new('http://127.0.0.1:5000')
    
if __name__ == "__main__":
    threading.Timer(1,open_browser).start()
    app.run(debug=True)