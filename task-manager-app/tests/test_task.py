import sys
import os
import unittest
from unittest.mock import mock_open , patch
from io import StringIO
from unittest.mock import patch
import unittest.mock
import json
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from task_manager.task import tasks_manger
from task_manager import user

tasks_data = '{"task_list": {"Complete the project": {"description": "Project description", "deadline": "2024-12-31", "priority": "red", "status": "Complete"}, "sleep": {"description": "go to sleep", "deadline": "2 days", "priority": "green", "status": "Complete"}}}'

class test_task(unittest.TestCase , user):

    @patch('builtins.open', new_callable=mock_open, read_data='{"Yusuf": {"task_list": {"Complete the project": {"description": "Project description", "deadline": "2024-12-31", "priority": "red", "status": "In progress"}}}}}')
    def setUp(self, mock_file):
        self.manager = tasks_manger("Yusuf")

    def test_load_user_data_success(self):
        expected = {
            "Complete the project": {
                "description": "Project description",
                "deadline": "2024-12-31",
                "priority": "red",
                "status": "In progress"
            }
        }
        self.assertEqual(self.manager.task_list, expected)

    @patch('builtins.open', new_callable=mock_open)
    def test_load_user_data_file_not_found(self, mock_file):
        mock_file.side_effect = FileNotFoundError
        manager = tasks_manger("Yusuf")
        self.assertEqual(manager.task_list, {})  # Should be an empty dict

    @patch('builtins.open', new_callable=mock_open, read_data='{"Yusuf": {"task_list": invalid_json"')
    def test_load_user_data_json_decode_error(self, mock_file):
        with self.assertRaises(json.JSONDecodeError):
            self.manager.load_user_data()  # Use the instance to call the method

    def test_edit_task(self):
        self.manager.task_list = {
            "Complete the project": {
                "description": "Project description",
                "deadline": "2024-12-31",
                "priority": "red",
                "status": "In progress"
            }
        }
        self.manager.target = "Complete the project"
        with patch('builtins.input', side_effect=["New description"]):
            self.manager.edit_task()
            self.assertEqual(self.manager.task_list["Complete the project"]["description"], "New description")

    def test_mark_complete(self):
        self.manager.task_list = {
            "Complete the project": {
                "description": "Project description",
                "deadline": "2024-12-31",
                "priority": "red",
                "status": "In progress"
            }
        }
        self.manager.target = "Complete the project"
        with patch('builtins.input', side_effect=["1"]):  # Simulate user saying "yes" to mark as complete
            result = self.manager.mark_complete()
            self.assertEqual(self.manager.task_list["Complete the project"]["status"], "Complete")
            self.assertEqual(result, "Complete")

    def test_delete_task(self):
        self.manager.task_list = {
            "Complete the project": {
                "description": "Project description",
                "deadline": "2024-12-31",
                "priority": "red",
                "status": "In progress"
            }
        }
        self.manager.target = "Complete the project"
        with patch('builtins.input', side_effect=["1"]):  # Simulate user confirming deletion
            self.manager.delete_task()
            self.assertNotIn("Complete the project", self.manager.task_list)

if __name__ == '__main__':
    unittest.main()