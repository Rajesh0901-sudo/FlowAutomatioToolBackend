from utils.db import Database
from flask import jsonify
from utils.db import Database

def handle_external_api_method(data):

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