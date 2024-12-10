import unittest
import sys
import os
from unittest.mock import mock_open, patch
import json

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from task_manager.subtask import SubTask
from task_manager.task import Tasks_manager

class TestSubTask(unittest.TestCase):
    @patch('builtins.input', side_effect=["1" , "1" ,"1"])
    def test_subtask_creation(self , mock_input):
        first = Tasks_manager("yswef" )
        reslt =first.add_subtask("love yswef")
        self.assertEqual(reslt , {"love yswef" : "In progress"})
        pass
    @patch('builtins.input', side_effect=["1" ,"1", "1" , "1"])
    def test_mark_subtask_complete(self , mock_input):
        task = Tasks_manager("yswef")
        subtask = SubTask("yswef")
        task.add_subtask("love yswef")
        first = subtask.mark_complete()
        self.assertEqual(first , 0)
    @patch('builtins.input', side_effect=["1" , "1","1" , "1" , "1" , "1" , "1"])
    def test_task_completion_with_subtasks(self , mock_input):
        task = Tasks_manager("yswef")
        subtask1 = SubTask("yswef" )
        task.add_subtask("love yswef")
        task.add_subtask("love asta")
        subtask1.mark_complete()
        subtask1.mark_complete()
        self.assertEqual(task.check_completion(), "Complete")

if __name__ == '__main__':
    unittest.main()
        