# test_subtask.py
import unittest
import sys
import os
from unittest.mock import mock_open, patch
import json

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from task_manager.subtask import SubTask

class TestSubTask(unittest.TestCase):

    def test_subtask_creation(self):
        subtask = SubTask("Subtask 1", "Details", "2024-10-31", "High")
        self.assertEqual(subtask.task_name, "Subtask 1")
        self.assertEqual(subtask.status, "In progress")

    def test_mark_subtask_complete(self):
        subtask = SubTask("Subtask 1", "Details", "2024-10-31", "High")
        subtask.mark_complete()
        self.assertEqual(subtask.status, "Complete")

    def test_task_completion_with_subtasks(self):
        task = Task("Main Task", "Main Task Description", "2024-11-01", "Medium")
        subtask1 = SubTask("Subtask 1", "Subtask 1 Details", "2024-10-30", "Low")
        subtask2 = SubTask("Subtask 2", "Subtask 2 Details", "2024-10-31", "Medium")
        
        task.add_subtask(subtask1)
        task.add_subtask(subtask2)
        
        # تحديد المهام الفرعية كمكتملة
        subtask1.mark_complete()
        subtask2.mark_complete()

        # التحقق من اكتمال المهمة الرئيسية
        self.assertEqual(task.check_completion(), "Complete")

if __name__ == '__main__':
    unittest.main()
        