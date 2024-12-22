import unittest
from utils.doc_generator import DocumentGenerator
import os

class TestDocumentGenerator(unittest.TestCase):
    def setUp(self):
        self.doc_generator = DocumentGenerator()
        self.test_file = "./data/test_query_results.docx"

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_save_results_to_docx(self):
        result = self.doc_generator.save_results_to_docx(
            "test_db", "test_flow", ["col1", "col2"], [("val1", "val2")], self.test_file
        )
        self.assertEqual(result, 1)
        self.assertTrue(os.path.exists(self.test_file))

if __name__ == '__main__':
    unittest.main()