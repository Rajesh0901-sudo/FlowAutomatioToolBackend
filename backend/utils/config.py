# config.py
import json
import os

class ConfigManager:
    def __init__(self):
        self.envs_file = os.path.join(os.path.dirname(__file__), "data", "new_envs.json")

    def env_file_exist(self):
        try:
            if not os.path.exists(self.envs_file):
                print(self.envs_file, "Configuration env file not found")
                return False
            return True
        except Exception as e:
            print("an error occurred while opening env files", e)
            return False

    def load_env_config(self, env_name):
        if not self.env_file_exist():
            return None

        try:
            with open(self.envs_file, "r") as file:
                envs = json.load(file)

            if env_name not in envs:
                print("env not found")
                return None

            return envs[env_name]
        except Exception as e:
            print("an error occurred while opening env files", e)
            return None

    def add_env_config(self, env_name, configurations):
        if not self.env_file_exist():
            return {"error": "Configuration env file not found"}

        try:
            with open(self.envs_file, "r") as file:
                envs = json.load(file)

            if env_name in envs:
                return {"error": "Environment already exists"}

            envs[env_name] = configurations

            with open(self.envs_file, "w") as file:
                json.dump(envs, file, indent=4)

            return {"message": "Environment added successfully"}
        except Exception as e:
            print("an error occurred while opening env files", e)
            return {"error": str(e)}

    def update_env_config(self, env_name, new_configurations):
        if not self.env_file_exist():
            return {"error": "Configuration env file not found"}

        try:
            with open(self.envs_file, "r") as file:
                envs = json.load(file)

            if env_name not in envs:
                return {"error": "Environment does not exist"}

            envs[env_name] = new_configurations

            with open(self.envs_file, "w") as file:
                json.dump(envs, file, indent=4)

            return {"message": "Environment updated successfully"}
        except Exception as e:
            print("an error occurred while opening env files", e)
            return {"error": str(e)}