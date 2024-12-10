# function start program
# you will write the logic necessary for starting up the app
from task_manager import user,task,subtask,pomodoro_timer,category,notification
import sys
from time import sleep
from datetime import datetime,time
import json
import threading

class Controller:
    
    def __init__(self) -> None:
        self.setup()
        self.user =user.User(self.User_name , self.User_password , self.User_log_phone)
        self.task = task.Tasks_manager(self.User_name)
        self.time_tracking = task.Time_tracking(self.User_name)
        self.subtask = subtask.SubTask(self.User_name)
        self.pomodoro = pomodoro_timer.Pomodoro_time()
        self.category = category
        self.time = (datetime.now().time()).minute
        pass
    
    def setup(self):
        for i in "\u001b[1m**        TASK MANAGER         **\u001b[0m\n":
            print(i , end="" ,flush=True)
            sleep(0.07)
        sleep(0.50)
        self.User_name = input("\033[46menter your name:\033[0m\n")
        if self.User_name != "test":
            self.User_password = user.User(self.User_name,None)._password_check()
            if self.User_password == False:
                print("\033[41m\033[1mI am sorry, but tha app will be turned off\nI hope to restart and log in again\033[0m")
                seconds = 10
                while seconds + 1:
                    mins, secs = divmod(seconds, 60)
                    timer = f"\033[1m{mins:02d}:{secs:02d}\033[0m"
                    print(f"{timer}", end="\r")
                    sleep(1)
                    seconds -= 1
                sys.exit()
                
            while True:
                print("\033[46menter loge phone use:\033[0m\n")
                print("    hours",end="\r")
                self.hours = input("")
                print("    minutes",end="\r")
                self.minutes = input("")
                if self.hours.isdigit() and self.minutes.isdigit():
                    m = int(self.minutes) // 60
                    self.hours = int(self.hours) + m
                    self.minutes = int(self.minutes) % 60
                    t = time(self.hours,self.minutes)
                    self.User_log_phone = t.strftime("%H:%M").lstrip('0')
                    break
                else:
                    print("The entered value is not a number.")
        else:
            self.User_password = "yswef want phone"
            self.User_log_phone = "00:00"
        return self.User_name,self.User_password,self.User_log_phone
    
    def start_program(self):
        text = """\n\n        \033[1m\033[31mTASK MENU \033[0m   
1.crate task       2.viwe task           3.edit task   
4.marke comblet    5.add subtske         6.log phone use  
7.pomodoro time    8.delete task         9.mark subtask complete  
10.time tracking   11.stop tracking      12.git time spent
13.reset time      14.task to category   15.change password
                                                    \033[31m0.[exit and save]\033[0m
    \n"""
        self.user.load_user_data()
        noti = notification
        thread = threading.Thread(target=(noti.Upcoming_deadlines(self.User_name).upcoming_deadlines(),noti.Overdue_tasks(self.User_name).overdue_tasks()))
        thread.start()
        while True:
            if (datetime.now().time()).minute == (self.time + 1):
                thr = threading.Thread(target=(noti.Productivity_tips().productivity_tips()))
                thr.start()
            self.user.save_user_data()
            for i in text:
                print(i , end="" ,flush=True)
                sleep(0.02)
            user_chooes = input("choose namber:\n")
            if user_chooes.isdigit() and int(user_chooes) <= 15:
                user_chooes = int(user_chooes)
                if user_chooes == 1 :#create task
                    self.user.create_task()
                    self.user.save_user_data()
                
                elif user_chooes == 2:#view tasks
                    self.user.view_tasks()
                
                elif user_chooes == 3:#edit task
                    self.task.edit_task()
                    self.task.save_user_data()
                
                elif user_chooes == 4:#mark tha task as complete
                    self.task.mark_complete()
                    self.task.save_user_data()
                
                elif user_chooes == 5:#add subtask for the task
                    sub = input("what is the subtask:\n")
                    self.task.add_subtask(sub)
                    self.task.save_user_data()
                
                elif user_chooes == 6:#print log phone usege
                    self.user.log_phone_usage()
                
                elif user_chooes == 7:#start pomodoro timer 
                    self.pomodoro.start_sessions()
                
                elif user_chooes == 8:#delete task 
                    self.task.delete_task()
                    self.task.save_user_data()
                
                elif user_chooes == 9:#mark subtask as complete
                    self.subtask.mark_complete()
                
                elif user_chooes == 10:#start time tracking 
                    self.time_tracking.start_timer()
                
                elif user_chooes == 11:#stop time tracking
                    self.time_tracking.stop_timer()
                
                elif user_chooes == 12:#git the spent time in time tracking
                    self.time_tracking.git_time_spent()
                
                elif user_chooes == 13:#reset the time tracking
                    self.time_tracking.reset_timer()
                
                elif user_chooes == 14:# show a task as categorys
                    s = self.js_to_da()
                    if s:
                        print("categorys:\n\t[1].work\n\t[2].study\n\t[3].Personal")
                        a = input("")
                        if a.isdigit() and int(a) <= 3 and int(a) >= 0 :
                            a = int(a)
                            if a == 1 :
                                categoryW =self.category.WorkTask(s[0],s[1],s[2],s[3]).task_info()
                                categorywP =self.category.WorkTask(s[0],s[1],s[2],s[3]).set_priority("Work")
                                print(f"\n\n{categoryW}")
                                print(categorywP)
                                sleep(2)
                            if a == 2 :
                                categoryS =self.category.StudyTask(s[0],s[1],s[2],s[3]).task_info()
                                categorySP =self.category.StudyTask(s[0],s[1],s[2],s[3]).set_priority("Study")
                                print(f"\n\n{categoryS}")
                                print(f"\n\n{categorySP}")
                                sleep(2)
                            if a == 3 :
                                categoryP =self.category.PersonalTask(s[0],s[1],s[2],s[3]).task_info()
                                categoryPp =self.category.PersonalTask(s[0],s[1],s[2],s[3]).set_priority("Personal")
                                print(f"\n\n{categoryP}")
                                print(f"\n\n{categoryPp}")
                                sleep(2)
                        else:
                            print("wrong choice")
                    
                elif user_chooes == 15:#change user password
                    old_password = user.User(self.User_name,self.User_password)._password_check()
                    if old_password != False:
                        print("now enter the new password")
                        new_password = user.User(None,None)._password_check()
                        self.User_password = new_password
                        self.user =user.User(self.User_name , self.User_password , self.User_log_phone)
                        self.user.save_user_data()
                    else :
                        print("Try again")
                    
                
                
                
                elif user_chooes == 0:#exit and save
                    self.user.save_user_data()
                    sys.exit()
                    break
            else:
                print("\033[31mthis number is incorrect, try again\033[0m")
    
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

