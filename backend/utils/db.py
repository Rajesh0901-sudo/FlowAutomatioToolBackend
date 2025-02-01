# db.py
from sqlalchemy import create_engine, text
import oracledb
from sqlalchemy.orm import sessionmaker
from .config import ConfigManager
from .queries import QueryExecutor
import os



class Database:
    def __init__(self, env_name):
        self.env_name = env_name
        self.omsSession = None
        self.abpSession = None
        self.crmSession = None
        

    def get_db_session(self,db_name):
        if not self.env_name:
            print("env name is null or empty")
            return None

        config_manager = ConfigManager()
        envConfFile = config_manager.load_env_config(self.env_name)

        if not envConfFile:
            print("env file not found")
            return None
        
        dirname = os.path.dirname(__file__)
        print(dirname)
        oracle_client_file = os.path.join(dirname, '../../Oracle_Instant_Client\instantclient_23_6')  
        print(oracle_client_file)


        print(type(envConfFile['db_host']), envConfFile['service_name'])
        oracledb.init_oracle_client(lib_dir=oracle_client_file)


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
        
        elif db_name == 'crm':
            connection_string = f"oracle+oracledb://SA:SA@{envConfFile['db_host']}:1521/{envConfFile['service_name']}"
            print("connection string is-", connection_string)
            try:
                engine = create_engine(connection_string)
                Session = sessionmaker(bind=engine)
                self.crmSession = Session()
                return self.crmSession
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



       

    def run_queries(self, db_name,flow_name,document_path,document_name,is_to_save_data_in_csv):

        try:
            self.get_db_session('oms')
            
            query_executor = QueryExecutor()

            if self.omsSession:
                query_executor.execute_queries(self.omsSession, 'oms',flow_name,document_path,document_name,is_to_save_data_in_csv)

            else:
                print("Failed to create a oms database session")

            self.get_db_session('crm')    

            if self.crmSession:
                query_executor.execute_queries(self.crmSession, 'crm',flow_name,document_path,document_name,is_to_save_data_in_csv)

            else:
                print("Failed to create a crm database session")    


            self.get_db_session('abp')

            if self.abpSession:
                query_executor.execute_queries(self.abpSession, 'abp',flow_name,document_path,document_name,is_to_save_data_in_csv)

            else:
                print("Failed to create a abp database session")
        except Exception as e:
            print("An error occured while running Queries. Error-",e)
        
        finally:
            if self.omsSession:
                self.omsSession.close()
                print("Closed oms session")
            else:
                print("No OMS Session Found")
            if self.abpSession:
                self.abpSession.close()
                print("Closed abp session")
            else:
                print("No ABP Session Found")
