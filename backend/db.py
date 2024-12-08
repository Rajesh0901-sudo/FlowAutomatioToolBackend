from sqlalchemy import create_engine,text
import oracledb
from doc_generator import save_results_to_docx
from sqlalchemy.orm import sessionmaker
from queries import execute_queries

oracledb.init_oracle_client(lib_dir="C:\Program Files (x86)\oracle\instantclient_23_6")
connection_string = "oracle+oracledb://OMS1OMS:OMS1OMS@illnqw7974:1521/CHRDB7936"


try:
    engine = create_engine(connection_string)
    Session = sessionmaker(bind=engine)

except Exception as e:
    print("An Error Occurred:",e)

def get_db_session():
    newSession = Session()
    return newSession


def main():
    newSession =  get_db_session()
    execute_queries(newSession)
    newSession.close()
    print("Closed session")

if __name__ == "__main__":
    main()



