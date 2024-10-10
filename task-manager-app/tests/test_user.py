import sys
import os
import unittest
from io import StringIO
from unittest.mock import patch
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))) 
from task_manager.user import user1

class test_user(unittest.TestCase ):

    def setUp(self):
        self.test_user1 =  user1("Yusuf", "yswef1234@!A" , 'Complete the project')
        
    @patch('builtins.input', return_value='Complete the project')
    def test_creat_task(self , mock_input):
        self.test_user1.create_task()
        
    def test_log_phone_usage(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.test_user1.log_phone_usage()
            self.assertIn('your phone usage is : 5:22', fake_out.getvalue())
    
    @patch('builtins.input', return_value="yswef1234@!A")
    def test_password_chack(self ,mock_input):
        a = self.test_user1.password_check()
        self.assertEqual(a , True , "it is not equai True")

    @patch('builtins.input', return_value="12")
    def test_password_chack0(self ,mock_input):
        a = self.test_user1.password_check()
        self.assertEqual(a , False , "it is not equai True")
    
    @patch('builtins.len', return_value="12")
    def test_view_tasks(self , mock_len):
        te = self.test_user1.view_tasks()
        self.assertEqual(te , True , "it is not equai True")
        
    def test_view_tasks(self ):
        te = self.test_user1.view_tasks()
        self.assertEqual(te , False , "it is not equai True")















