import unittest
from utils.prepare_queries import QueryPreparer
import os
import json

class TestQueryPreparer(unittest.TestCase):
    def setUp(self):
        self.query_preparer = QueryPreparer()
        self.customer_details_file = "./data/test_customer_details.json"
        with open(self.customer_details_file, 'w') as f:
            json.dump({"CreateCustomerResponse": {"ID": "12345"}}, f)

    def tearDown(self):
        os.remove(self.customer_details_file)

    def test_prepare_queries(self):
        queries = self.query_preparer.prepare_queries()
        self.assertEqual(len(queries), 2)
        self.assertIn("select CTDB_CRE_DATETIME", queries[0])
        self.assertIn("select CHARGE_ID", queries[1])

if __name__ == '__main__':
    unittest.main()