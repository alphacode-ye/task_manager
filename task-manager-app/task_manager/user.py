import re
import time
import json


class user1:
    def __init__(self, user_name, password1=None):
        self.user_name = user_name
        self.log_phone_usa = "5:22"
        self.password = password1
        self.task_list = {}
        self.task_priorityS = ("red", "yellow", "green")
        self.load_user_data()  
    
    def create_task(self):
        print("hi " + self.user_name)
        time.sleep(1)
        self.new_task = input("What is your new target?\n")
        self.task_descrip = input("Write me a description of your mission to remember\n")
        self.task_deadlien = input("Set a deadline for the task.\n")
        self.status = ("In progress")
        priority = input("What is the danger of the mission [1 = red, 2 = yellow, 3 = green]\n")
        self.new_task_priority = self.task_priorityS[int(priority) - 1]
        self.task_list[self.new_task] = {
            "description": self.task_descrip,
            "deadline": self.task_deadlien,
            "priority": self.new_task_priority,
            "status" : self.status
        }
        self.save_user_data()
    
    def view_tasks(self):
        if self.task_list:
            print("Your tasks:")
            a = 1
            for task_name, details in self.task_list.items():
                print("Task "+ str(a) +" : " + task_name)
                print("  Description: " + details["description"])
                print("  Deadline: " + details["deadline"])
                print("  Priority: " + details["priority"])
                print("  status: " + details["status"])
                print("-" * 20)
                a = a + 1
            print("Total tasks you have: " + str(len(self.task_list)))
            return True
        else:
            print("No task found")
            return "No task found"
        
    def log_phone_usage(self):
        print("Your phone usage is: " + self.log_phone_usa)
    
    def password_check(self):
        self.stop = True
        while self.stop:
            self.password = input("Enter password:\n")
            if re.fullmatch(r'[A-Za-z0-9@!$%^&+=]{8,}', self.password):
                time.sleep(1)
                print("Your password is strong like you, my friend")
                time.sleep(1)
                print("Good luck")
                self.stop = False
                self.save_user_data()  
                return True
            else:
                print("I'm sorry, my friend, but your password is weak")
                time.sleep(1)
                print("You must use special symbols, uppercase and lowercase letters, and numbers.")
                return False
            
    def save_user_data(self):
        try:
            with open('data\\data.json', 'r') as file:
                user_data = json.load(file)
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
            pass




