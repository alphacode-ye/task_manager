# report_generator.py
from task_manager import data_base
import os


class Report:
    def __init__(self, user_name, password, log_phone_use):
        self.user = user_name
        self.password = password
        self.log_phone = log_phone_use
        self.DATA = data_base.Data(self.user, self.password, self.log_phone)
        pass

    def generate_productivity_report(
        self,
    ):  # انشاء تقرير كامل عن المستخدم واخراجة كملف نصي
        if not os.path.exists(r"C:\Users\yusef\Documents\Task manager"):
            os.makedirs(r"C:\Users\yusef\Documents\Task manager")
        file = input("inter name report file:\n")
        Complete = self.DATA.git_tasks("Complete")
        In_progress = self.DATA.git_tasks("In progress")
        with open(
            rf"C:\Users\yusef\Documents\Task manager\{file}.txt", "+w", encoding="utf-8"
        ) as txt:
            report = f"""Name: {self.user}
Pasword: {self.password}
Phone use: {self.log_phone}
Totel tasks: {Complete + In_progress}
Complete tasks: {Complete}
In progress: {In_progress}
            """
            txt.write(report)
        pass
