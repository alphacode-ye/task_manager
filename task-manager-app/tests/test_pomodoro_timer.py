import unittest
import sys
import os
from unittest.mock import patch , MagicMock , Mock
import json
from task_manager import pomodoro_timer
from task_manager import notification



class Test_pomodoro_timer(unittest.TestCase):
    
    def setUp(self):
        self.test_pomodoro_times = pomodoro_timer.Pomodoro_time()
        self.notifications = notification.Notifications()
        self.test_pomodoro_times.work_time = 10
        self.test_pomodoro_times.short_brake_time = 10
        self.test_pomodoro_times.notif = MagicMock()
    
    def test_start_timer_to_work(self):
        test_timer = self.test_pomodoro_times.start_timer(self.test_pomodoro_times.work_time)
        self.assertEqual(test_timer, "00:00")
    
    def test_start_timer_to_brake_time(self):
        test_timer = self.test_pomodoro_times.start_timer(self.test_pomodoro_times.short_brake_time)
        self.assertEqual(test_timer, "00:00")
    
    
    @patch('builtins.print')
    @patch('time.sleep', return_value=None)
    def test_start_sessions(self, mock_sleep, mock_print ):
        resalt = self.test_pomodoro_times.start_sessions()
        
        self.assertTrue(mock_print.called)
        self.test_pomodoro_times.notif.app_notification.assert_called()
        
        self.assertIn(resalt , ["break time end" , "all sessions done"])
        
    



if __name__ == '__main__':
    unittest.main()