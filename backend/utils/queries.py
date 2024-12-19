from sqlalchemy import text
from doc_generator import save_results_to_docx
import json,os
from prepareQueries import prepare_queries


query_file = "./data/queries.json"

def query_file_exist():
    try:
        if not os.path.exists(query_file):
            print(query_file,"query_file not found")
            return False
        
        else:
            return True
    
    except Exception as e:
        print("an error occured while opening query_file",e)
        return False
    
def load_queries(db_name,flow_name):

    if query_file_exist() != True:
        return None

    try:

        with open (query_file,"r") as file:
            queries = json.load(file)

        if db_name not in queries:
            print("query related to db not found")
            return None
        
        print(queries)
        return queries[db_name][flow_name]
    
    except Exception as e:
        print("an error occured while opening env files-",e)



def execute_queries(session,db_name,flow_name):

    if session == ('',None):
        print("No db session exist")
        return 0

    print("session connected succesfully")

    queries = prepare_queries()

    for query in queries:
        result = session.execute(text (query))
        rows = result.fetchall() 
        column_name = result.keys()
        print("Query executed succesfully")

        print(f"{' | '.join(column_name)}")
        
        for row in rows:
            print(row) 

        save_results_to_docx(db_name,flow_name,column_name,rows)
    
    
