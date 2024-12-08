from sqlalchemy import create_engine,text
import oracledb
from doc_generator import save_results_to_docx
from sqlalchemy.orm import sessionmaker
from queries import execute_queries
from config import load_env_config



def get_db_session(env_name):

    if env_name == ('',None):
        print("env name is null or emmpty")
        return 0

    envConfFile = load_env_config(env_name)

    if envConfFile == None:
        print("env file not found")
        return 0
    
    print(type(envConfFile['db_user_name']),envConfFile['db_user_name'])


    oracledb.init_oracle_client(lib_dir="C:\Program Files (x86)\oracle\instantclient_23_6")
    #connection_string = "oracle+oracledb://OMS1OMS:OMS1OMS@illnqw7974:1521/CHRDB7936"
    connection_string = 'oracle+oracledb://'+envConfFile['db_user_name']+':'+envConfFile['db_password']+'@'+envConfFile['db_host']+':1521/'+envConfFile['service_name']

    print("connection string is-",connection_string)


    try:
        engine = create_engine(connection_string)
        Session = sessionmaker(bind=engine)

    except Exception as e:
        print("An Error Occurred:",e)
    
    newSession = Session()
    return newSession


def main():
    newSession =  get_db_session("illnqw7936")
    execute_queries(newSession)
    newSession.close()
    print("Closed session")

if __name__ == "__main__":
    main()



