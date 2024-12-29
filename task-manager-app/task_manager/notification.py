# notification.py
import threading
from playsound import playsound
from plyer import notification
from datetime import datetime
from random import randrange
import json
from task_manager.user import Encrypt


class Notifications:
    def sound(self):
        playsound(
            "task_manager/media/sound.wav"
        )  # ضع مسار اي مقطع صوتي بامتداد(.wav)لتغيير النغمة الخاصة بالاشعار

    def app_notification(self, message, tim):#هنا يجب ادخال الرسالة المراد ضهورها في الاشعار ومدة الظهور 
        notification.notify(
            title="Task Manager",#تغيير عنوان الاشعار 
            message=message,
            app_name="Task Manager",#تغيير اسم التطبيق في الاشعار 
            app_icon="task_manager/media/icon.ico",#هنا تستطيع تغيير ايقونة الاشعار بتغير مسار الصورة الي مسار الصورة الجديد التي تريدها 
            timeout=tim,
            toast=False,
        )  # عرض الاشعار
        yswef = threading.Thread(target=self.sound())
        yswef.start()
        return "notification is sandeng"


class Upcoming_deadlines:  # ارسال الاشعار لكل المهمات المتبقي لها اقل من خمسة ايام
    def __init__(self, user_name):
        self.user = user_name
        self.note = Notifications()
        self.encrypt = Encrypt()
        pass

    def upcoming_deadlines(self):
        with open("data/data.json", "r+") as file:
            key = self.encrypt.load_key()
            user_data = json.load(file)
            data = self.encrypt.decrypt_data(user_data,key)
            task = data.get(self.user, {}).get("task_list", {}).keys()
            for i in task:
                taskd = (
                    data.get(self.user, {})
                    .get("task_list", {})
                    .get(i, {})
                    .get("deadline")
                )
                dead = datetime.strptime(taskd, "%Y-%m-%d").date()
                h = (dead - datetime.now().date()).days
                if h < 5 and h > 0:
                    message = f"The deadline for the task {i} in {h} days left"
                    self.note.app_notification(message, 10)


class Overdue_tasks:  # ارسال اشعار للمهامات المتاخرة
    def __init__(self, user_name):
        self.user = user_name
        self.note = Notifications()
        self.encrypt = Encrypt()
        pass

    def overdue_tasks(self):
        with open("data/data.json", "r+") as file:
            key = self.encrypt.load_key()
            user_data = json.load(file)
            data = self.encrypt.decrypt_data(user_data,key)
            task = data.get(self.user, {}).get("task_list", {}).keys()
            for i in task:
                taskd = (
                    data.get(self.user, {})
                    .get("task_list", {})
                    .get(i, {})
                    .get("deadline")
                )
                dead = datetime.strptime(taskd, "%Y-%m-%d").date()
                h = (dead - datetime.now().date()).days
                if h < 0:
                    message = f"you are late for {i} get it done today"
                    self.note.app_notification(message, 10)


class Productivity_tips:  # كلاس ارسال اشعارات تحفيزية
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
            "You are unique, and the world needs what you have to offer.",
        ]
        self.note = Notifications()
        pass

    def productivity_tips(self):  # ارسال اشعارات تحفيزية
        i = randrange(0, 20)
        message = f"{self.motivational_phrases[i]}"
        self.note.app_notification(message, 10)
