import unittest
from task_manager.category import WorkTask, PersonalTask, StudyTask

class TestTaskCategory(unittest.TestCase):
    def test_work_task_info(self):
        task = WorkTask("Project Meeting", "Discuss project milestones", "2024-11-01", "High" )
        self.assertEqual(
            task.task_info(),
            "Work Task: Project Meeting\n Description: Discuss project milestones\n Deadline: 2024-11-01\n Priority: High"
        )

    def test_personal_task_info(self):
        task = PersonalTask("Gym", "Attend gym session", "2024-11-02", "Medium")
        self.assertEqual(
            task.task_info(),
            "Personal Task: Gym\n Description: Attend gym session\n Deadline: 2024-11-02\n Priority: Medium"
        )

    def test_study_task_info(self):
        task = StudyTask("Math Revision", "Revise calculus", "2024-11-03", "High")
        self.assertEqual(
            task.task_info(),
            "Study Task: Math Revision\n Description: Revise calculus\n Deadline: 2024-11-03\n Priority: High"
        )

    def test_set_priority(self):
        task = WorkTask("Project Meeting", "Discuss project milestones", "2024-11-01", "Low")
        task.set_priority("High")
        self.assertEqual(task.priority, "High")

if __name__ == "__main__":
    unittest.main()