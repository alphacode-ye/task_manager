#user class user.py
import re
import time
import json
from datetime import datetime

class User:
    def __init__(self, user_name, password1 ="password1" , log_phone_use ="5:22"):
        self.user_name = user_name
        self.log_phone_usa = log_phone_use
        # users must have passwords can't be null
        self.password = password1
        self.task_list = {}
        self.task_priorityS = ("Red", "Yellow", "Green")
        # should be in its own class
        self.load_user_data()  
    
    def create_task(self):
        print("hi " + self.user_name)
        time.sleep(1)
        # be clear about your inputs UX
        self.new_task = input("Enter the title of the new task?\n")
        self.task_descrip = input("Write a description of the task.\n")
        # deadline should be Datetime input 
        while True:
            user_input = input("enter didline(yyyy-mm-dd):\n")
            try:
                self.task_deadlien = datetime.strptime(user_input, "%Y-%m-%d" ).date()
                if self.task_deadlien >= datetime.now().date():
                    break
                else:
                    print("The task should not be in the past.")
                    pass
            except:
                print("You have entered the wrong format. It should be like (yyyy-mm-dd):")
                pass
        # should be enum
        self.status = ("In progress")
        # edit your question UX
        priority = input("Enter task important [\u001b[31m1 = red,\u001b[33m 2 = yellow,\u001b[32m 3 = green\u001b[0m]\n")
        self.new_task_priority = self.task_priorityS[int(priority) - 1]
        
        self.task_list[self.new_task] = {
            "task" : self.new_task , 
            "description": self.task_descrip,
            "deadline": self.task_deadlien,
            "priority": self.new_task_priority,
            "status" : self.status,
            "subtask": []
        }
        # self.save_user_data()
    
    def view_tasks(self):
        if self.task_list:
            print("\033[1m\033[31m\033[4mYour tasks:\033[0m")
            a = 1
            for task_name, details in self.task_list.items():
                print("\033[1mTask \033[31m"+ str(a) +"\033[0m : " + task_name)
                print("\033[0m\033[3m   Description: " + details["description"])
                print("   Deadline: " + details["deadline"])
                print("   Priority: " + details["priority"])
                print("   status: " + details["status"])
                print("\033[0m\033[1m-" * 30 + "\033[0m")
                a = a + 1
            print("Total tasks you have: " + str(len(self.task_list)))
            return True
        else:
            print("No task found")
            return "No task found"
        
    def log_phone_usage(self):
        print("Your phone usage is: " + self.log_phone_usa)
    
    def _password_check(self):
        self.stop = True
        wronge = 0
        while self.stop:
            self.password = input("Enter password:\n")
            if re.fullmatch(r'[A-Za-z0-9@!$%^&+=]{8,}', self.password):
                time.sleep(1)
                print("Your password is strong.")
                time.sleep(1)
                print("Good luck")
                self.stop = False
                # self.save_user_data()  
                return self.password
            else:
                print("I'm sorry, my friend, but your password is weak")
                print("You must use special symbols, uppercase and lowercase letters,numbers, and 8 chars .")
                wronge += 1
                if wronge ==3:
                    print("\033[31myour attempts to log in is over \033[0m")
                    return False
            
    def save_user_data(self):
        # if vs try - catch
        try:
            with open('data\\data.json', 'r') as file:
                
                user_data = json.load(file)
                #########
        except (json.JSONDecodeError, FileNotFoundError):
            user_data = {}
            
        user_data[self.user_name] = {
            "name": self.user_name,
            "password": self.password,
            "log_phone_usa": self.log_phone_usa,
            "task_list": self.task_list
        }
        with open('data\\data.json', 'w') as file:
            json.dump(user_data, file, indent=4)
        return self.task_list
        
    def load_user_data(self):
        try:
            with open('data\\data.json', 'r') as file:
                user_data = json.load(file)
                user_info = user_data.get(self.user_name, {})
                self.password = user_info.get("password", self.password)
                self.log_phone_usa = user_info.get("log_phone_usa", self.log_phone_usa)
                self.task_list = user_info.get("task_list", {})
            
        except (json.JSONDecodeError, FileNotFoundError):
            with open('data\\data.json', "w") as file:
                return None
            pass
        


#you should apply object to json & json to object 

