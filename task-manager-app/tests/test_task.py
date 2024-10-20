import unittest
import sys
import os
from unittest.mock import mock_open, patch
import json

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'task_manager')))
from task_manager.task import tasks_manager
from task_manager.user import user1

class TestTaskManager(unittest.TestCase):

    @patch('builtins.open', new_callable=mock_open, read_data='{"Yusuf": {"task_list": {"Complete the project": {"description": "Project description", "deadline": "2024-12-31", "priority": "red", "status": "In progress"}}}}')
    def setUp(self, mock_file):
        self.manager = tasks_manager("Yusuf")

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
        manager = tasks_manager("Yusuf")
        self.assertEqual(manager.task_list, {})

    @patch('builtins.open', new_callable=mock_open, read_data='{"Yusuf": {"task_list": invalid_json"')
    def test_load_user_data_json_decode_error(self, mock_file):
        self.manager.load_user_data()
        self.assertEqual(self.manager.task_list, {})

    def test_edit_task_success(self):
        self.manager.task_list = {
            "Complete the project": {
                "description": "Project description",
                "deadline": "2024-12-31",
                "priority": "red",
                "status": "In progress"
            }
        }
        self.manager.target = "Complete the project"
        with patch('builtins.input', side_effect=["1", "New description"]):
            result = self.manager.edit_task()
            self.assertEqual(self.manager.task_list["Complete the project"]["description"], "New description")
            self.assertTrue(result)

    def test_edit_task_invalid_input(self):
        self.manager.task_list = {
            "Complete the project": {
                "description": "Project description",
                "deadline": "2024-12-31",
                "priority": "red",
                "status": "In progress"
            }
        }
        self.manager.target = "Complete the project"
        with patch('builtins.input', side_effect=["invalid input"]):
            result = self.manager.edit_task()
            self.assertEqual(result, "error")

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
        with patch('builtins.input', side_effect=["1"]):
            result = self.manager.mark_complete()
            self.assertEqual(self.manager.task_list["Complete the project"]["status"], "Complete")
            self.assertEqual(result, "Complete")

    def test_delete_task_success(self):
        self.manager.task_list = {
            "Complete the project": {
                "description": "Project description",
                "deadline": "2024-12-31",
                "priority": "red",
                "status": "In progress"
            }
        }
        self.manager.target = "Complete the project"
        with patch('builtins.input', side_effect=["1"]):
            result = self.manager.delete_task()
            self.assertNotIn("Complete the project", self.manager.task_list)
            self.assertEqual(result, "done")

    def test_delete_task_invalid_input(self):
        self.manager.task_list = {
            "Complete the project": {
                "description": "Project description",
                "deadline": "2024-12-31",
                "priority": "red",
                "status": "In progress"
            }
        }
        self.manager.target = "Complete the project"
        with patch('builtins.input', side_effect=["invalid input"]):
            result = self.manager.delete_task()
            self.assertEqual(result, "error")

if __name__ == '__main__':
    unittest.main()
