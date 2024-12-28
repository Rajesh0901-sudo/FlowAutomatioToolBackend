import unittest
from utils.add_data_in_json import DataManager
import os
import json

class TestDataManager(unittest.TestCase):
    def setUp(self):
        self.data_manager = DataManager()
        self.envs_file = "./data/test_envs.json"
        self.customer_details_file = "./data/test_customer_details.json"
        # Create test files
        with open(self.envs_file, 'w') as f:
            json.dump({}, f)
        with open(self.customer_details_file, 'w') as f:
            json.dump({}, f)

    def tearDown(self):
        # Remove test files
        os.remove(self.envs_file)
        os.remove(self.customer_details_file)

    def test_add_env_config(self):
        result = self.data_manager.add_env_config("test_env", {"db_user_name": "test_user"})
        self.assertEqual(result, {"message": "Environment added successfully"})
        with open(self.envs_file, 'r') as f:
            envs = json.load(f)
        self.assertIn("test_env", envs)

    def test_add_customer_details(self):
        result = self.data_manager.add_customer_details({"CreateCustomerResponse": {"ID": "12345"}})
        self.assertEqual(result, {"message": "Customer details added successfully"})
        with open(self.customer_details_file, 'r') as f:
            customer_details = json.load(f)
        self.assertIn("CreateCustomerResponse", customer_details)

if __name__ == '__main__':
    unittest.main()