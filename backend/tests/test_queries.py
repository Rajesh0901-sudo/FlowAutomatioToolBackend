import unittest
from unittest.mock import MagicMock
from utils.queries import QueryExecutor
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import os
import json

class TestQueryExecutor(unittest.TestCase):
    def setUp(self):
        self.query_executor = QueryExecutor()
        self.query_executor.query_file = "./data/test_queries.json"
        with open(self.query_executor.query_file, 'w') as f:
            json.dump({"test_db": {"test_flow": ["SELECT 1"]}}, f)

    def tearDown(self):
        os.remove(self.query_executor.query_file)

    def test_load_queries(self):
        queries = self.query_executor.load_queries("test_db", "test_flow")
        self.assertEqual(queries, ["SELECT 1"])

    def test_execute_queries(self):
        session = MagicMock()
        self.query_executor.load_queries = MagicMock(return_value=["SELECT 1"])
        self.query_executor.execute_queries(session, "test_db", "test_flow")
        session.execute.assert_called_with("SELECT 1")

if __name__ == '__main__':
    unittest.main()