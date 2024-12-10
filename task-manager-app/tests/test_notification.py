import unittest
from unittest.mock import patch , MagicMock , Mock
from task_manager import pomodoro_timer
from task_manager.notification import Productivity_tips,Notifications,Upcoming_deadlines,Overdue_tasks

class Test_Notifications(unittest.TestCase):
    
    def setUp(self):
        self.notifications = Notifications()
        self.notifications.notif = MagicMock()



