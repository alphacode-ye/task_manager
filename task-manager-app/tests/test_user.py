import sys
import os
import unittest
from unittest.mock import mock_open
from io import StringIO
from unittest.mock import patch
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from task_manager.user import user1

class TestUser(unittest.TestCase):

    def setUp(self):
        self.test_user1 = user1("Yusuf", "yswef1234")
    
    @patch('builtins.open', new_callable=mock_open)
    @patch('builtins.input', side_effect=['Complete the project', 'Project description', '2024-12-31', '1' , ""])
    def test_create_task(self, mock_input , mock_open):
        self.test_user1.create_task()
        self.assertIn('Complete the project', self.test_user1.task_list)
        self.assertEqual(self.test_user1.task_list['Complete the project']['description'], 'Project description')
        self.assertEqual(self.test_user1.task_list['Complete the project']['deadline'], '2024-12-31')
        self.assertEqual(self.test_user1.task_list['Complete the project']['priority'], 'red')

    def test_log_phone_usage(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.test_user1.log_phone_usage()
            self.assertIn('Your phone usage is: 5:22', fake_out.getvalue())

    @patch('builtins.open', new_callable=mock_open)
    @patch('builtins.input', return_value="yswef1234")
    def test_password_check_success(self, mock_input , mock_open):
        a = self.test_user1.password_check()
        self.assertEqual(a, True, "Password check did not return True for a strong password")

    @patch('builtins.input', return_value="12345")
    def test_password_check_failure(self, mock_input):
        a = self.test_user1.password_check()
        self.assertEqual(a, False, "Password check did not return False for a weak password")

    def test_view_tasks_with_tasks(self):
        self.test_user1.task_list = {
            'Task 1': {'description': 'Description 1', 'deadline': '2024-12-31', 'priority': 'red' ,"status" : "combelet"}
        }
        te = self.test_user1.view_tasks()
        self.assertEqual(te, True, "Expected True when there are tasks")

    def test_view_tasks_no_tasks(self):
        self.test_user1.task_list = {}  # تأكد من أن قائمة المهام فارغة
        te = self.test_user1.view_tasks()
        self.assertEqual(te, "No task found" , "Expected False when there are no tasks")


if __name__ == '__main__':
    unittest.main()
