import unittest
from unittest.mock import *
from task_manager import task
from task_manager.task import Tasks_manager , Time_tracking
import time

class TestTasksManager(unittest.TestCase):
    pass


class TestTime_Tracking(unittest.TestCase):
    def setUp(self):
        self.time = Time_tracking("Yusuf")
        
    def test_start_timer(self):
        self.time.start_time = 2.0
        resilt = self.time.start_timer()
        self.assertEqual(resilt , 2.0 , "the time is start")
        
    
    def test_stop_timer(self):
        self.time.start_time = time.time()
        resilt = self.time.stop_timer()
        self.assertEqual(resilt , 0 )
    
    def test_git_time_spent(self):
        self.time.time_spent = 2.0
        resilt = self.time.git_time_spent()
        self.assertEqual(resilt , f"\033[1m00:02\033[0m time spent in this task." , "the time is not coracet")

    def test_reset_timer(self):
        resilt = self.time.reset_timer()
        self.assertEqual(resilt[0] , 0 , "time spint is not reset")
        self.assertEqual(resilt[1] , None , "start time is not reset")
        
    

if __name__ == '__main__':
    unittest.main()
