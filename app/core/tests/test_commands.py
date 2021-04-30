# Going to stimulate a database for testing, this is also called as mocking

from unittest.mock import patch
from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import TestCase


class CommandsTestCase(TestCase):
    def test_wait_for_db_ready(self):
        """Test waiting for db when db is available"""
        with patch('django.db.utils.ConnectionHandler.__getitem__') as gi:  # argument inside the patch is the command called when database is connected check docs
            gi.return_value = True  # Making database connection true without connecting it helps us in testing, this is known as mocking
            call_command('wait_for_db')  # this checks folder called for management in our root director and executes the wait_for_db files inside it
            self.assertEqual(gi.call_count, 1)

    @patch('time.sleep', return_value=None)
    def test_wait_for_db(self, ts):
        """Test waiting for db"""
        with patch('django.db.utils.ConnectionHandler.__getitem__') as gi:
            gi.side_effect = [OperationalError] * 5 + [True]
            call_command('wait_for_db')
            self.assertEqual(gi.call_count, 6)
