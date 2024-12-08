from sqlalchemy import text
from doc_generator import save_results_to_docx


def execute_queries(session):

    if session is ('',None):
        print("No db session exist")
        return 0

    print("session connected succesfully")

    result = session.execute(text ("select CTDB_CRE_DATETIME, ORDER_UNIT_ID, ORDER_ID, STATUS, ACTION_TYPE, AP_ID, reason_id, customer_id,sales_channel  from tborder_action where customer_id = '1000000438' order by CTDB_CRE_DATETIME asc"))
    rows = result.fetchall() 
    column_name = result.keys()
    
    print("Query executed succesfully")

    print(f"{' | '.join(column_name)}")
    
    for row in rows:
        print(row) 

    save_results_to_docx(column_name,rows)