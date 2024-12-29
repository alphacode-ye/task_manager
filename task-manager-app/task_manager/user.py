# user class user.py
import re 
import time
import os
import json
import base64
from datetime import datetime
from cryptography.fernet import Fernet

class User:
    def __init__(self, user_name, password1=None, log_phone_use="5:22"):
        self.user_name = user_name
        self.log_phone_usa = log_phone_use
        # users must have passwords can't be null
        self.password = password1
        self.task_list = {}
        self.task_priorityS = ("Red", "Yellow", "Green")
        self.encrypt = Encrypt()
        # should be in its own class
        self.load_user_data()

    def create_task(self):  # انشاء مهمهة
        print("hi " + self.user_name)
        time.sleep(1)
        # be clear about your inputs UX
        self.new_task = input("Enter the title of the new task?\n")  # اسم المهمة
        self.task_descrip = input("Write a description of the task.\n")  # وصف المهمة
        # deadline should be Datetime input
        while True:
            user_input = input("enter didline(yyyy-mm-dd):\n")
            try:
                self.task_deadlien = datetime.strptime(user_input, "%Y-%m-%d").date()
                if self.task_deadlien >= datetime.now().date():
                    break
                else:
                    print("The task should not be in the past.")
                    pass
            except:
                print(
                    "You have entered the wrong format. It should be like (yyyy-mm-dd):"
                )
                pass
        # should be enum
        self.status = "In progress"
        # edit your question UX
        priority = input(
            "Enter task important [\u001b[31m1 = Red,\u001b[33m 2 = Yellow,\u001b[32m 3 = Green\u001b[0m]\n"
        )
        self.new_task_priority = self.task_priorityS[int(priority) - 1]

        self.task_list[self.new_task] = {
            "task": self.new_task,
            "description": self.task_descrip,
            "deadline": f"{self.task_deadlien}",
            "priority": self.new_task_priority,
            "status": self.status,
            "subtask": [],
        }
        # self.save_user_data()

    def view_tasks(self):  # عرض المهمات بشكل مرتب ومنسق وملون
        if self.task_list:
            print("\033[1m\033[31m\033[4mYour tasks:\033[0m")
            a = 1
            for task_name, details in self.task_list.items():
                print("\033[1mTask \033[31m" + str(a) + "\033[0m : " + task_name)
                print("\033[0m\033[3m   Description: " + details["description"])
                print("     Deadline: " + details["deadline"])
                print("     Priority: " + details["priority"])
                print("     status: " + details["status"])
                print("\033[0m\033[1m-" * 50 + "\033[0m")
                a = a + 1
            print("Total tasks you have: " + str(len(self.task_list)))
            return True
        else:
            print("No task found")
            return "No task found"

    def log_phone_usage(self):
        print("Your phone usage is: " + str(self.log_phone_usa))

    def _password_check(self):  # التحقق من  قوة الباسورد
        self.stop = True
        wronge = 0  # متغير للعد كم مرة اخطئ في كتابة الرمز
        while self.stop:
            self.password = input("\033[46mEnter password:\033[0m\n")
            if self.old_password == None:  # اذا لم يكن هناك باسورد قديم يتم انشاء واحد
                if re.fullmatch(
                    r"[A-Za-z0-9@!$%^&+=_ ]{8,}", self.password
                ):  # التحق اذا الرمز كان 8 احرف ويحتوي على الرموز الخاصة والمسافات
                    time.sleep(1)
                    print("Your password is strong.")
                    time.sleep(1)
                    print("Good luck")
                    self.stop = False
                    # self.save_user_data()
                    return self.password
                else:
                    print("I'm sorry, my friend, but your password is weak")
                    print(
                        "You must use special symbols, uppercase and lowercase letters,numbers, and 8 chars ."
                    )
                    wronge += 1
                    if wronge == 3:
                        print("\033[31myour chansses to log in is over \033[0m")
                        return False
            elif (
                self.password == self.old_password
            ):  # اذا كان هناك باسورد قديم يتم من التحقق هل الرمز المدخل نفس الباسورد القديم
                print("Good luck")
                self.stop = False
                return self.password
            else:
                print("I'm sorry, my friend, but this is not your password")
                wronge += 1
                if wronge == 3:
                    print("\033[31myour attempts to log in is over \033[0m")
                    return False

    def save_user_data(
        self,
    ):  # يجب استخدام هاذي الدالة في نهاية الكود لكي يتم حفظ التغيرات التي حصلت في الدوال السابقة
        # if vs try - catch
        try:
            with open("data\\data.json", "r") as file:
                user_data = json.load(file)
                key = self.encrypt.load_key()
                user_data = json.load(file)
                data = self.encrypt.decrypt_data(user_data,key)
                #
        except (json.JSONDecodeError, FileNotFoundError):
            user_data = {}
        
        user_data[self.user_name] = {
            "name": self.user_name,
            "password": self.password,
            "log_phone_usa": self.log_phone_usa,
            "task_list": self.task_list,
        }
        key = self.encrypt.load_key()
        data = self.encrypt.encrypt_data(user_data,key)
        with open("data\\data.json", "w") as file:
            json.dump(data, file, indent=4)
        return self.task_list

    def load_user_data(
        self,
    ):  # سيتم استخدام هاذي الدالة تلقائي في بداية الكلاس عند استدعائة
        try:
            with open("data\\data.json", "+r") as file:
                key = self.encrypt.load_key()
                user_data = json.load(file)
                data = self.encrypt.decrypt_data(user_data,key)
                user_info = data.get(self.user_name, {})
                self.old_password = user_info.get("password", self.password)
                # self.log_phone_usa = user_info.get("log_phone_usa", self.log_phone_usa)
                self.task_list = user_info.get("task_list", {})
                return 1

        except (json.JSONDecodeError, FileNotFoundError):
            with open("data\\data.json", "+r") as file: 
                json.dump({},file)
                self.old_password = None
                return None
            pass

class Encrypt ():
    def generate_key(self):
        return Fernet.generate_key()
    
    def save_key(self,key, filename="secret.key"):
        with open(filename, "wb") as key_file:
            key_file.write(key)
    def load_key(self,filename="secret.key"):
        if not os.path.exists(filename):
            key = self.generate_key()
            self.save_key(key, filename)
        else:
                key = open(filename, "rb").read()
                return key
        
    def encrypt_data(self,data, key):
        try:
            if isinstance(data, dict):  # إذا كانت البيانات قاموس
                data = json.dumps(data)  # تحويل القاموس إلى نص JSON
            fernet = Fernet(key)
            encrypted_data = fernet.encrypt(data.encode())  # تشفير النص
            return base64.urlsafe_b64encode(encrypted_data).decode()
        except BaseException as a:
            print(a)
            pass
    
    def decrypt_data(self,encrypted_data, key):
        try :
            encrypted_data = base64.urlsafe_b64decode(encrypted_data.encode())  # تحويل النص إلى bytes
            fernet = Fernet(key)
            decrypted_data = fernet.decrypt(encrypted_data).decode()  # فك التشفير
            try:
                return json.loads(decrypted_data)  # محاولة تحويل النص إلى JSON (إذا كان مناسبًا)
            except json.JSONDecodeError:
                return decrypted_data 
        except:
            pass

# you should apply object to json & json to object
if __name__ == "__main__":
    u = User("yswef","i love asta", "12:55")
    key = Encrypt()
    e = key.load_key()
    # o = key.encrypt_data(a , e)
    # print(o)