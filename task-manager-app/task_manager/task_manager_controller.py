# function start program
# you will write the logic necessary for starting up the app
from task_manager import user,task,subtask,pomodoro_timer,category
import sys
from time import sleep
import json

class Controller:
    
    def __init__(self) -> None:
        self.setup()
        self.user =user.User(self.User_name , self.User_password , self.User_log_phone)
        self.task = task.Tasks_manager(self.User_name)
        self.time_tracking = task.Time_tracking(self.User_name)
        self.subtask = subtask.SubTask(self.User_name)
        self.pomodoro = pomodoro_timer.Pomodoro_time()
        self.category = category
        pass
    
    def setup(self):
        for i in "\u001b[1m**        TASK MANAGER         **\u001b[0m\n":
            print(i , end="" ,flush=True)
            sleep(0.07)
        sleep(0.50)
        self.User_name = input("\033[46menter your name:\033[0m\n")
        
        self.User_password = user.User(None,None)._password_check()
        if self.User_password == False:
            print("\033[41m\033[1mI am sorry, but tha app will be turned off\ni hope to restart and loge in again\033[0m")
            seconds = 10
            while seconds + 1:
                mins, secs = divmod(seconds, 60)
                timer = f"\033[1m{mins:02d}:{secs:02d}\033[0m"
                print(f"{timer}", end="\r")
                sleep(1)
                seconds -= 1
            sys.exit()
        
        self.User_log_phone = input("\033[46menter loge phone use:\033[0m\n")
        return self.User_name,self.User_password,self.User_log_phone
    
    def start_program(self):
        text = """\n\n        \033[1m\033[31mTASK MENU \033[0m   
1.crate task       2.viwe task        3.edit task   
4.marke comblet    5.add subtske      6.log phoneus  
7.pomodoro time    8.delete task      9.mark subtask complete  
10.time tracking   11.stop tracking   12.git time spent
13.reset time 
                                                    0.[exit]
    \n"""
        while True:
            for i in text:
                print(i , end="" ,flush=True)
                sleep(0.02)
            user_chooes = input("choose namber:\n")
            self.user.load_user_data()
            if user_chooes.isdigit() and int(user_chooes) <= 20:
                user_chooes = int(user_chooes)
                if user_chooes == 1 :
                    self.user.create_task()
                elif user_chooes == 2:
                    self.user.view_tasks()
                elif user_chooes == 3:
                    self.task.edit_task()
                elif user_chooes == 4:
                    self.task.mark_complete()
                elif user_chooes == 5:
                    self.task.add_subtask()
                elif user_chooes == 6:
                    self.user.log_phone_usa()
                elif user_chooes == 7:
                    self.pomodoro.start_sessions()
                elif user_chooes == 8:
                    self.task.delete_task()
                elif user_chooes == 9:
                    self.subtask.mark_complete()
                elif user_chooes == 10:
                    self.subtask.mark_complete()
                elif user_chooes == 11:
                    self.time_tracking.stop_timer()
                elif user_chooes == 12:
                    self.time_tracking.git_time_spent()
                elif user_chooes == 13:
                    self.time_tracking.reset_timer()
                elif user_chooes == 14:
                    s = self.js_to_da()
                    a =self.category.WorkTask(s[0],s[1],s[2],s[3]).task_info()
                    print(f"\n\n{a}")
                    sleep(1)
                    
                
                
                
                
                elif user_chooes == 0:
                    self.user.save_user_data()
                    break
            else:
                print("this number is incorrect, try again")
        pass
    
    def js_to_da(self):
        try:
            with open("data/data.json", 'r+') as file:
                self.user_data = json.load(file)
                o = self.task.define_the_mission()
                if o != None:
                    task = self.user_data.get(self.User_name, {}).get('task_list', {}).get(o ,{}).get("task")
                    description = self.user_data.get(self.User_name, {}).get('task_list', {}).get(o ,{}).get("description")
                    deadline = self.user_data.get(self.User_name, {}).get('task_list', {}).get(o ,{}).get("deadline")
                    priority = self.user_data.get(self.User_name, {}).get('task_list', {}).get(o ,{}).get("priority")
                    return [task , description, deadline, priority]
                else:
                    return None
                
            
        except (json.JSONDecodeError, FileNotFoundError):
            with open('data\\data.json', "w") as file:
                return None
            pass


f = Controller()
f.start_program()
