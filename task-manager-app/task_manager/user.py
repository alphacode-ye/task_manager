class user1:
    import re
    import time
    
    def __init__(self, user_name , password):
        self.user_name = user_name
        self.task_list = []
        self.log_phone_usa = "5:22"
    
    def create_task(self , new_task):
        self.task_list.append(new_task)
    
    def view_tasks(self):
        try:
            self.num = 1
            for task in self.task_list:
                print(str(self.num)+ task)
                self.num =+ 1
        except ImportError:
            print("no task found ")
    
    def log_phone_usage(self):
        print("your phone usage is : "+self.log_phone_usa)
    
    def password_check(self):
        self.stop = True
        while self.stop:
            self.password = input("enter password:\n")
            if re.fullmatch(r'[A-Za-z0-9@!$%^&+=]{8,}', self.password): 
                print("\n")
                time.sleep(1)
                print("your password is strong like you my frind")
                time.sleep(1)
                print("Good luck")
                self.stop = False
                
            else:
                print("I'm sorry, my friend, but your password is weak")
                time.sleep(1)
                print("You must use special symbols, uppercase and lowercase letters, and numbers.")
                print("Thanks")

                