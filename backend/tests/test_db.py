import unittest
from utils.db import Database
from unittest.mock import patch, MagicMock

class TestDatabase(unittest.TestCase):
    @patch('utils.db.ConfigManager')
    @patch('utils.db.create_engine')
    def test_get_db_session(self, mock_create_engine, MockConfigManager):
        mock_config_manager = MockConfigManager.return_value
        mock_config_manager.load_env_config.return_value = {
            'db_user_name': 'test_user',
            'db_password': 'test_pass',
            'db_host': 'test_host',
            'service_name': 'test_service'
        }
        mock_engine = mock_create_engine.return_value
        mock_sessionmaker = MagicMock()
        mock_sessionmaker.return_value = MagicMock()
        mock_create_engine.return_value = mock_engine
        mock_engine.connect.return_value = mock_sessionmaker

        db = Database('test_env')
        session = db.get_db_session()
        self.assertIsNotNone(session)

    @patch('utils.db.QueryExecutor')
    @patch('utils.db.Database.get_db_session')
    def test_run_queries(self, mock_get_db_session, MockQueryExecutor):
        mock_session = MagicMock()
        mock_get_db_session.return_value = mock_session
        mock_query_executor = MockQueryExecutor.return_value

        db = Database('test_env')
        db.run_queries('test_db', 'test_flow')
        mock_query_executor.execute_queries.assert_called_with(mock_session, 'test_db', 'test_flow')
        mock_session.close.assert_called_once()

if __name__ == '__main__':
    unittest.main()