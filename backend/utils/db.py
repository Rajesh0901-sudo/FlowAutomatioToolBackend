# db.py
from sqlalchemy import create_engine, text
import oracledb
from sqlalchemy.orm import sessionmaker
from utils.config import ConfigManager
from utils.queries import QueryExecutor

class Database:
    def __init__(self, env_name):
        self.env_name = env_name
        self.session = None

    def get_db_session(self):
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
        connection_string = f"oracle+oracledb://{envConfFile['db_user_name']}:{envConfFile['db_password']}@{envConfFile['db_host']}:1521/{envConfFile['service_name']}"

        print("connection string is-", connection_string)

        try:
            engine = create_engine(connection_string)
            Session = sessionmaker(bind=engine)
            self.session = Session()
            return self.session
        except Exception as e:
            print("An Error Occurred:", e)
            return None

    def run_queries(self, db_name, flow_name):
        self.get_db_session()
        if self.session:
            query_executor = QueryExecutor()
            query_executor.execute_queries(self.session, db_name, flow_name)
            self.session.close()
            print("Closed session")
        else:
            print("Failed to create a database session")

