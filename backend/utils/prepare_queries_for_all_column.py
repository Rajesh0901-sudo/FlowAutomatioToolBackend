# prepare_queries.py
import json
import os

class CSVQueryPreparer:
    def __init__(self):
        self.customer_details_file = "./data/customer_details.json"
        self.query_details_file = "./data/queries.json"

    def file_exist(self,file_name):
        try:
            if not os.path.exists(file_name):
                print(self.file_name, "query_file not found")
                return False
            return True
        except Exception as e:
            print("an error occurred while opening {file_name}", e)
            return False

    def load_queries(self,db_name,flow_name):
        if not self.file_exist(self.query_details_file):
            return None

        try:
            with open(self.query_details_file, "r") as file:
                query_details = json.load(file)

            return query_details.get(db_name).get(flow_name)
        
        except Exception as e:
            print("an error occurred while opening query details files-", e)
            return None
        
    def load_customers(self):
        if not self.file_exist(self.customer_details_file):
            return None

        try:
            with open(self.customer_details_file, "r") as file:
                customer_details = json.load(file)

            return customer_details
        except Exception as e:
            print("an error occurred while opening customer files-", e)
            return None

    def prepare_queries(self,db_name,flow_name):

        if not self.file_exist(self.query_details_file):
            return None
        
        param_details = self.load_customers()
        queries = []

        print("preparing Query")

        #customer_id = customer_details.get('ID')
        #account_id = customer_details.get('customerAccountId')

        query_details_data = self.load_queries(db_name,flow_name)

        print(type(query_details_data),query_details_data)


        for query_row in query_details_data:
            print("query is - ", query_row["params"][0])
            print("query is - ",  query_row["query"])

            print("query is - ",  query_row["query"])

            query = query_row["query"]

            print(param_details.get(query_row["params"][0]))

            for param in query_row["params"]:
                query = query.replace(f":{param}",param_details[param])
                print("query is - ", query)
                queries.append((query_row["table_name"], query))


        print("All Queries Are-",queries)

        return queries