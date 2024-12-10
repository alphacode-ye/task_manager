import threading
from playsound import playsound
from plyer import notification
from datetime import datetime
from random import randrange
import json
from time import sleep

class Notifications():
    def sound(self):
        playsound('task_manager/media/sound.wav')
    
    def app_notification(self, message , tim ):
        notification.notify(
            title="Task Manager",
            message=message,
            app_name="Task Manager",
            app_icon='task_manager/media/icon.ico',
            timeout=tim,
            toast=False
        )
        yswef = threading.Thread(target=self.sound())
        yswef.start()
        return "notification is sandeng"
    

class Upcoming_deadlines():
    def __init__(self , user_name):
        self.user = user_name
        self.note = Notifications()
        pass
    
    def upcoming_deadlines(self):
        with open("data/data.json", 'r+') as file:
            user_data = json.load(file)
            task = user_data.get(self.user, {}).get('task_list', {}).keys()
            for i in task:
                taskd = user_data.get(self.user, {}).get('task_list', {}).get(i , {}).get("deadline")
                dead =   datetime.strptime(taskd, "%Y-%m-%d" ).date()
                h = (dead - datetime.now().date()).days
                if h < 5 and h > 0 :
                    message = f"The deadline for the task {i} in {h} days left"
                    self.note.app_notification(message,10)
                
            
    

class Overdue_tasks():
    def __init__(self , user_name):
        self.user = user_name
        self.note = Notifications()
        pass
    
    def overdue_tasks(self):
        with open("data/data.json", 'r+') as file:
            user_data = json.load(file)
            task = user_data.get(self.user, {}).get('task_list', {}).keys()
            for i in task:
                taskd = user_data.get(self.user, {}).get('task_list', {}).get(i , {}).get("deadline")
                dead =   datetime.strptime(taskd, "%Y-%m-%d" ).date()
                h = (dead - datetime.now().date()).days
                if h < 0 :
                    message = f"you are late for {i} get it done today"
                    self.note.app_notification(message,10)


class Productivity_tips():
    def __init__(self):
        self.motivational_phrases = [
        "Believe in yourself and all that you are.",
        "Every day is a new opportunity to grow and improve.",
        "Don't be afraid to make mistakes; they help you learn.",
        "Keep going, even if it feels hard; you're getting stronger.",
        "Dream big and don't let anyone limit you.",
        "You are capable of amazing things!",
        "Small steps lead to big achievements.",
        "Every effort you make is progress toward your goal.",
        "Stay positive, work hard, and enjoy the journey.",
        "Your potential is endless; keep pushing forward.",
        "Mistakes are proof that you're trying.",
        "You have the power to make a difference.",
        "Set your goals high, and don't stop until you reach them.",
        "Believe that you can, and you're halfway there.",
        "You're stronger than you think.",
        "Be proud of every step you take toward your dreams.",
        "You are braver, stronger, and smarter than you know.",
        "The more you practice, the better you'll get.",
        "Keep smiling, keep trying, and never give up!",
        "You are unique, and the world needs what you have to offer."
        ]
        self.note = Notifications()
        pass
    
    def productivity_tips(self):
            i = randrange(0, 20)
            message = f"{self.motivational_phrases[i]}"
            self.note.app_notification(message,10)
            
    
# a = (datetime.now().time()).hour
# m = (datetime.now().time()).second
# if m >=30:
#     al = 1 + a
#     print(al)   
#     mins, secs = divmod(al, 60)
# else:
#     mins, secs = divmod(a, 60)
# print(a)
# print(m)
# print(f"{mins}  +  {secs}")
# # Productivity_tips().productivity_tips()
# i = 0
# p = 300
# o = 0
# # while p - 1:
# #     i += 1
# #     p -= 1
# #     if i == 60:
# #         i = 0
# #         print(f"**  {p}  **")
# #     elif i == a:
# #         o += 1
# #         print(f"--  **{o}**  --")



# if (datetime.now().time()).minute == a:
#     print("**  i love asta  **")
#     Productivity_tips().productivity_tips()

