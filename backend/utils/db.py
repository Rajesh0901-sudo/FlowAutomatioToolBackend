# db.py
from sqlalchemy import create_engine, text
import oracledb
from sqlalchemy.orm import sessionmaker
from utils.config import ConfigManager
from utils.queries import QueryExecutor

class Database:
    def __init__(self, env_name):
        self.env_name = env_name
        self.omsSession = None
        self.abpSession = None
        

    def get_db_session(self,db_name):
        if not self.env_name:
            print("env name is null or empty")
            return None

        config_manager = ConfigManager()
        envConfFile = config_manager.load_env_config(self.env_name)
        if not envConfFile:
            print("env file not found")
            return None

        print(type(envConfFile['db_user_name']), envConfFile['db_user_name'])
        oracledb.init_oracle_client(lib_dir="C:\\Program Files (x86)\\oracle\\instantclient_23_6")


        if db_name == 'oms':
            connection_string = f"oracle+oracledb://OMS1OMS:OMS1OMS@{envConfFile['db_host']}:1521/{envConfFile['service_name']}"
            print("connection string is-", connection_string)
            try:
                engine = create_engine(connection_string)
                Session = sessionmaker(bind=engine)
                self.omsSession = Session()
                return self.omsSession
            except Exception as e:
                print("An Error Occurred:", e)
                return None


        elif db_name == 'abp':
            connection_string = f"oracle+oracledb://ABPAPP1:ABPAPP1@{envConfFile['db_host']}:1521/{envConfFile['service_name']}"
            print("connection string is-", connection_string)
            try:
                engine = create_engine(connection_string)
                Session = sessionmaker(bind=engine)
                self.abpSession = Session()
                return self.abpSession
            except Exception as e:
                print("An Error Occurred:", e)
                return None
            
        else:
            print("Please select correct db")
            return None



       

    def run_queries(self, db_name,flow_name):
        self.get_db_session('oms')
        query_executor = QueryExecutor()

        if self.omsSession:
            query_executor.execute_queries(self.omsSession, 'oms',flow_name)
            self.omsSession.close()
            print("Closed oms session")
        else:
            print("Failed to create a oms database session")

        self.get_db_session('abp')
        if self.abpSession:
            query_executor.execute_queries(self.abpSession, 'abp',flow_name)
            self.abpSession.close()
            print("Closed abp session")
        else:
            print("Failed to create a abp database session")

