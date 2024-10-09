import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))) 

from task_manager.user import user1

name = "yswef"
user_run = user1(name , None ,None )

user_run.password_check()
user_run.view_tasks()
user_run.create_task()
user_run.view_tasks()
user_run.log_phone_usage()