import unittest
from unittest.mock import patch 
from task_manager import pomodoro_timer

class TestPomodoro_timer(unittest.TestCase):
    
    @patch('time.sleep', return_value=None)
    def test_start_timer_to_work(self , mock_sleep):
        self.test_pomodoro_times = pomodoro_timer.Pomodoro_time()
        self.test_pomodoro_times.work_time = 5
        test_timer = self.test_pomodoro_times.start_timer(self.test_pomodoro_times.work_time)
        self.assertEqual(test_timer, "00:00")
    
    @patch('time.sleep', return_value=None)
    def test_start_timer_to_brake_time(self , mock_sleep):
        self.test_pomodoro_times = pomodoro_timer.Pomodoro_time()
        self.test_pomodoro_times.short_brake_time = 5
        test_timer = self.test_pomodoro_times.start_timer(self.test_pomodoro_times.short_brake_time)
        self.assertEqual(test_timer, "00:00")
    
    
    @patch('time.sleep', return_value=None)
    def test_start_sessions(self, mock_sleep):
        self.test_pomodoro_times = pomodoro_timer.Pomodoro_time()
        self.test_pomodoro_times.work_time = 5
        self.test_pomodoro_times.short_brake_time = 5
        resalt = self.test_pomodoro_times.start_sessions()
        
        self.assertIn(resalt , ["break time end" , "all sessions done"])
        
    

if __name__ == '__main__':
    unittest.main()