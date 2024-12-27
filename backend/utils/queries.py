# queries.py
from sqlalchemy import text
from utils.doc_generator import save_results_to_docx
import json
import os
from utils.prepare_queries import QueryPreparer

class QueryExecutor:
    def __init__(self):
        self.query_file = "./data/queries.json"

    def query_file_exist(self):
        try:
            if not os.path.exists(self.query_file):
                print(self.query_file, "query_file not found")
                return False
            return True
        except Exception as e:
            print("an error occurred while opening query_file", e)
            return False

    def load_queries(self, db_name, flow_name):
        if not self.query_file_exist():
            return None

        try:
            with open(self.query_file, "r") as file:
                queries = json.load(file)

            if db_name not in queries:
                print("query related to db not found")
                return None

            return queries[db_name][flow_name]
        except Exception as e:
            print("an error occurred while opening query_file", e)
            return None

    def execute_queries(self, session, db_name, flow_name,document_path,document_name):
        if not session:
            print("No db session exists")
            return 0

        print("session connected successfully")

        query_preparer = QueryPreparer()
        queries = query_preparer.prepare_queries(db_name)

        for queryTuple in queries:
            tableName,query = queryTuple
            result = session.execute(text(query))
            rows = result.fetchall()
            column_names = result.keys()
            print("Query executed successfully")

            print(f"{' | '.join(column_names)}")

            for row in rows:
                print(row)

            save_results_to_docx(db_name, tableName, column_names, rows,document_path,document_name)