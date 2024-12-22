import unittest
from utils.check_existing_file import FileChecker
import os

class TestFileChecker(unittest.TestCase):
    def setUp(self):
        self.file_checker = FileChecker()
        self.test_file = "./data/test_file.txt"

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_check_file_status_existing(self):
        with open(self.test_file, 'w') as f:
            f.write("test")
        status = self.file_checker.check_file_status(self.test_file)
        self.assertEqual(status, 1)

    def test_check_file_status_non_existing(self):
        status = self.file_checker.check_file_status(self.test_file)
        self.assertEqual(status, 2)

if __name__ == '__main__':
    unittest.main()