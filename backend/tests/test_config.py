import unittest
from utils.config import ConfigManager
import os
import json

class TestConfigManager(unittest.TestCase):
    def setUp(self):
        self.config_manager = ConfigManager()
        self.envs_file = "./data/test_envs.json"
        # Create test file
        with open(self.envs_file, 'w') as f:
            json.dump({}, f)

    def tearDown(self):
        # Remove test file
        os.remove(self.envs_file)

    def test_add_env_config(self):
        result = self.config_manager.add_env_config("test_env", {"db_user_name": "test_user"})
        self.assertEqual(result, {"message": "Environment added successfully"})
        with open(self.envs_file, 'r') as f:
            envs = json.load(f)
        self.assertIn("test_env", envs)

    def test_update_env_config(self):
        self.config_manager.add_env_config("test_env", {"db_user_name": "test_user"})
        result = self.config_manager.update_env_config("test_env", {"db_user_name": "updated_user"})
        self.assertEqual(result, {"message": "Environment updated successfully"})
        with open(self.envs_file, 'r') as f:
            envs = json.load(f)
        self.assertEqual(envs["test_env"]["db_user_name"], "updated_user")

if __name__ == '__main__':
    unittest.main()