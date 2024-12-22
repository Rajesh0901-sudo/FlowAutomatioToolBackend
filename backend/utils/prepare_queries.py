# prepare_queries.py
import json
import os

class QueryPreparer:
    def __init__(self):
        self.customer_details_file = "./data/customer_details.json"

    def file_exist(self):
        try:
            if not os.path.exists(self.customer_details_file):
                print(self.customer_details_file, "query_file not found")
                return False
            return True
        except Exception as e:
            print("an error occurred while opening query_file", e)
            return False

    def load_customers(self):
        if not self.file_exist():
            return None

        try:
            with open(self.customer_details_file, "r") as file:
                customer_details = json.load(file)

            return customer_details
        except Exception as e:
            print("an error occurred while opening env files-", e)
            return None

    def prepare_queries(self):
        customer_details = self.load_customers()
        queries = []
        customer_id = customer_details.get('CreateCustomerResponse', {}).get('ID')
        if customer_id:
            query1 = f"select CTDB_CRE_DATETIME, ORDER_UNIT_ID, ORDER_ID, STATUS, ACTION_TYPE, AP_ID, reason_id, customer_id from tborder_action where customer_id = '{customer_id}' order by CTDB_CRE_DATETIME asc"
            query2 = f"select CHARGE_ID, CTDB_CRE_DATETIME, TYPE, DESCRIPTION, ACTUAL_PRICE, ORIGINAL_PRICE from tbbilling_Charge where ap_item_id in (select ap_id from tbap_price_plan where order_Action_id='21814') order by description desc"

            queries.append(query1)
            queries.append(query2)

        return queries