# add_data_in_json.py
import json
import os

class DataManager:
    def load_json(self, file_path):
        if not os.path.exists(file_path):
            return {}
        try:
            with open(file_path, 'r') as file:
                return json.load(file)
        except Exception as e:
            print(f"An error occurred while loading {file_path}: {e}")
            return {}

    def save_json(self, file_path, data):
        try:
            with open(file_path, 'w') as file:
                json.dump(data, file, indent=4)
        except Exception as e:
            print(f"An error occurred while saving {file_path}: {e}")

    def add_env_config(self, env_name, configurations):
        envs_file = "./data/new_envs.json"
        envs = self.load_json(envs_file)
        #if env_name in envs:
        #    return {"error": "Environment already exists"}
        envs[env_name] = configurations
        self.save_json(envs_file, envs)
        return {"message": "Environment added successfully"}

    def add_customer_details(self, customer_details):
        customer_details_file = "./data/customer_details.json"
        data = self.load_json(customer_details_file)
        data.update(customer_details)
        self.save_json(customer_details_file, data)
        return {"message": "Customer details added successfully"}
    
    def add_query_results(self, query_results_data):
        query_results_file = "./data/query_results.json"
        data = self.load_json(query_results_file)
        data.update(query_results_file)
        self.save_json(query_results_file, data)
        return {"message": "query_results_ added successfully"}