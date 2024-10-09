import re
import time

class user1:

    def __init__(self, user_name ,password ,new_task):
        self.user_name = user_name
        self.task_list = []
        self.log_phone_usa = "5:22"
        self.password = password
        self.new_task = new_task
    
    def create_task(self ):
        print("hi" + self.user_name)
        time.sleep(1)
        self.new_task = input("what is your new target?\n")
        self.task_list.append(self.new_task)
    
    def view_tasks(self):
        lin = len(self.task_list)
        if lin > 0:
            self.num = 1
            for task in self.task_list:
                print(str(self.num)+" "+ task)
                self.num =+ 1
            time.sleep(1)
            print("totel tasks you have \n" + str(self.num))
        else:
            print("no task found ")
    
    def log_phone_usage(self):
        print("your phone usage is : "+self.log_phone_usa)
    
    def password_check(self):
        self.stop = True
        while self.stop:
            self.password = input("enter password:\n")
            if re.fullmatch(r'[A-Za-z0-9@!$%^&+=]{8,}', self.password): 
                time.sleep(1)
                print("your password is strong like you my frind")
                time.sleep(1)
                print("Good luck")
                self.stop = False
                
            else:
                print("I'm sorry, my friend, but your password is weak")
                time.sleep(1)
                print("You must use special symbols, uppercase and lowercase letters, and numbers.")
                

                