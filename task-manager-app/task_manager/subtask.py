# subtask.py
from task_manager.task import Tasks_manager


class SubTask:
    def __init__(self, username,password):
        self.Tasks_manager = Tasks_manager(username,password)
        self.Tasks_manager.load_user_data()
        self.subtasks = []

    def mark_complete(self):  # جعل المهمة الفرعية كمنجزة
        try:
            i = []
            self.Tasks_manager.define_the_mission()  # تحديد المهمة التي فيها المهمة الفرعية المطلوبة
            for sub in self.Tasks_manager.task_list[self.Tasks_manager.target][
                "subtask"
            ]:
                for s in sub.keys():  # عرض المهمات الفرعية لكي يختار منها المستخدم
                    self.subtasks.append(s)
                if sub:
                    for i in range(len(self.subtasks)):
                        print(f"{i +1}.{self.subtasks[i]}")
                dtask = int(input("enter tha task you finsh it.\n"))
            self.Tasks_manager.task_list[self.Tasks_manager.target]["subtask"][
                dtask - 1
            ][self.subtasks[dtask - 1]] = "Complete"
            self.Tasks_manager.check_completion()  # بعد الاضافة يتم التشييك هل المهمات الفرعية منجزة ام لا
            self.Tasks_manager.save_user_data()
            return 0
        except BaseException as a:
            # print(a)
            print("no subtask is found")
            return None

