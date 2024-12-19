from flask import Flask, request, jsonify
from utils.add_data_in_json import add_env_config, add_customer_details

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

#@app.route('/get_evidence', methods=['POST'])
#def add_env():
    #file_data = request.json

    #if not file_data:
     #   return jsonify({"error": "Missing file details"}), 400

    #result = get_evidence(file_data)
    #return jsonify(result), 200

if __name__ == "__main__":
    app.run(debug=True)


