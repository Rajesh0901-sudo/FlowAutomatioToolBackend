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

    def prepare_queries(self,db_name):
        customer_details = self.load_customers()
        queries = []
        customer_id = customer_details.get('CreateCustomerResponse', {}).get('ID')
        account_id = customer_details.get('CreateCustomerResponse', {}).get('customerAccountId')

        if customer_id and db_name=='oms' :
            query1 = f"select CTDB_CRE_DATETIME, ORDER_UNIT_ID, ORDER_ID, STATUS, ACTION_TYPE, AP_ID, reason_id, customer_id from tborder_action where customer_id = '{customer_id}' order by CTDB_CRE_DATETIME asc"
            query2 = f"select CHARGE_ID, CTDB_CRE_DATETIME, TYPE, DESCRIPTION, ACTUAL_PRICE, ORIGINAL_PRICE from tbbilling_Charge where ap_item_id in (select ap_id from tbap_price_plan where order_Action_id='21814') order by description desc"

            queries.append(query1)
            queries.append(query2)

            '{account_id}'
            '{customer_id}'
        
        elif customer_id and db_name=='abp' and account_id :

            query1 = f"select SUB_STATUS,L9_NICK_NAME,L9_LINEAP_ID,PRIM_RESOURCE_VAL,SUBSCRIBER_NO,CUSTOMER_ID,EFFECTIVE_DATE from subscriber where customer_id = '{customer_id}' order by sys_creation_date desc"
            query2 = f"select ACCOUNT_ID,AR_BALANCE,ACCOUNT_STATUS,WRITE_OFF_STATUS,COLLECTION_INDICATOR,CUSTOMER_NO from ar1_account where customer_no='{customer_id}' order by sys_creation_date desc"
            query3 = f"select PAYMENT_ID,AMOUNT,TRANSACTION_ID,DEPOSIT_DATE,ACCOUNT_ID from ar1_payment_details where account_id='{account_id}' order by sys_creation_date desc"
            query4 = f"select ACCOUNT_ID,INVOICE_ID,CHARGE_CODE,AMOUNT,TAX_AMOUNT,CREDIT_REASON,CREDIT_LEVEL_CODE,BALANCE_IMPACT_CODE,CHG_REVENUE_CODE from ar1_customer_credit where account_id='{account_id}' order by sys_creation_date desc"
            query5 = f"select ACCOUNT_ID,INVOICE_ID,CHARGE_CODE,AMOUNT,TAX_AMOUNT,L3_PHYSICAL_ITEM_ID from ar1_charges where account_id='{account_id}' order by sys_creation_date desc"
            query6 = f"select L9_DYNAMIC_ATTRIBUTES,ACCOUNT_ID,STATUS,PHYSICAL_ITEM_ID,ORDER_ACTION_ID from AR3_ORDER_REFERENCE a where ACCOUNT_ID = '{account_id}' order by SYS_CREATION_DATE desc"
            query7 = f"select EIP_ID,Customer_ID,subscriber_id,Total_inst_no, DEVICE_PLAN_START_DATE,DEVICE_PLAN_END_DATE,plan_status,total_amount,TOTAL_BILLED_AMOUNT,BILLED_INST_NO from bl9_installment_plan where customer_id='{customer_id}' order by sys_creation_date desc"
            query8 = f"select EIP_ID,plan_status,total_amount,TOTAL_BILLED_AMOUNT,BILLED_INST_NO,exchanged_eip,DPP_TYPE,OFFER_ID,getdynacs(DYNAMIC_ATTRIBUTES,'IMEI') imei,ACCELERATE_IND,getdynacs(DYNAMIC_ATTRIBUTES,'accReason') AccReason,getdynacs(DYNAMIC_ATTRIBUTES,'Remaining balance') RemBalance,OFFER_INSTANCE_ID from bl9_installment_plan  where customer_id='{customer_id}' order by sys_creation_date desc"
            query9 = f"select CHARGE_CODE, EFFECTIVE_DATE,EXPIRATION_DATE, AMOUNT, SERVICE_RECEIVER_ID, RECEIVER_CUSTOMER, PAY_CHANNEL_NO, CYCLE_CODE, getdyna(dynamic_attributes,'IMEI') as IMEI from bl1_rc_rates where RECEIVER_CUSTOMER='{customer_id}' order by sys_creation_date desc"
            query10 = f"Select count(*),CHARGE_CODE,AMOUNT from bl1_charge_request  where RECEIVER_CUSTOMER= '{customer_id}' group by CHARGE_CODE,AMOUNT"


            queries.append(query1)
            queries.append(query2)
            queries.append(query3)
            queries.append(query4)
            queries.append(query5)
            queries.append(query6)
            queries.append(query7)
            queries.append(query8)
            queries.append(query9)
            queries.append(query10)


        return queries