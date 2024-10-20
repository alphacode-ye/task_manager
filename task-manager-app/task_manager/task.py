import json
import time
import os
from user import user1

class tasks_manager(user1):
    
    def __init__(self, user_name) -> None:
        self.user_name = user_name
        self.target = None
        self.load_user_data()

    def get_data_file_path(self):
        return os.path.join(os.path.dirname(__file__), '..', 'data', 'data.json')

    def load_user_data(self):
        try:
            with open(self.get_data_file_path(), 'r+') as file:
                self.user_data = json.load(file)
                self.task_list = self.user_data.get(self.user_name, {}).get('task_list', {})
                return self.task_list
        except (json.JSONDecodeError, FileNotFoundError):
            self.user_data = {}
            self.task_list = {}

    def define_the_mission(self):
        self.load_user_data()
        try:
            if self.task_list:
                self.view_tasks()
                all_tasks = list(self.task_list.keys())
                target_number = input("Enter the task number:\n")
                if target_number.isdigit():
                    target_number = int(target_number)
                    if 1 <= target_number and  int(target_number) - 1 <= len(all_tasks):
                        self.target = all_tasks[target_number - 1]
                        return self.target
                    else:
                        print("Task number out of range.")
                        self.target = None
                        return "error"
                else:
                    print("Invalid input. Please enter a number.")
                    self.target = None
                    return "error"
            else:
                self.target = None
                print("No tasks available.")
                return None
        except (IndexError, ValueError):
            self.target = None
            return "error"

    def edit_task(self):
        self.define_the_mission()
        if self.target and self.target != "error":
            task_keys = [key for key in self.task_list[self.target] if key != "status"]
            try:
                for index, key in enumerate(task_keys):
                    print(f"{index + 1}. {key}: **{self.task_list[self.target][key]}**")
                    time.sleep(1)
                edit_part = input("What do you want to change?[1.description , 2.deadline , 3.priority]\n")
                if edit_part.isdigit() and 1 <= int(edit_part) and int(edit_part) - 1 <= len(task_keys):
                    new_value = input("Write the new value\n")
                    self.task_list[self.target][str(task_keys[int(edit_part) - 1])] = new_value
                    self.save_user_data()
                    print("Change done.")
                    return True
                else:
                    print("Invalid selection.")
                    return "error"
            except ValueError:
                print("Invalid input.")
                return "error"
        elif self.target is None:
            print("No task found to change")
            return "error"
        else:
            print("No task with this number.")
            return "error"

    def mark_complete(self):
        self.define_the_mission()
        if self.target and self.target != "error":
            try:
                check = input("Are you done with this task?[1.yes , 2.No]\n")
                if check == "1":
                    self.task_list[self.target]["status"] = "Complete"
                    self.save_user_data()
                    return "Complete"
                elif check == "2":
                    self.task_list[self.target]["status"] = "In progress"
                    self.save_user_data()
                    return "In progress"
                else:
                    print("Invalid value. Please choose 1 or 2.")
                    return "error"
            except ValueError:
                print("Invalid input.")
                return "error"
        else:
            print("No task found")
            return "error"

    def delete_task(self):
        self.define_the_mission()
        if self.target and self.target != "error":
            try:
                sure = input("Are you sure you want to delete this task?[1.yes , 2.No]\n")
                if sure == "1":
                    del self.task_list[self.target]
                    self.save_user_data()
                    print("Task deleted successfully.")
                    return "done"
                elif sure == "2":
                    return "In progress"
                else:
                    print("Invalid value. Please choose 1 or 2.")
                    return "error"
            except ValueError:
                print("Invalid input.")
                return "error"
        else:
            print("No task found")
            return "error"

    def save_user_data(self):
        try:
            with open(self.get_data_file_path(), 'r') as file:
                user_data = json.load(file)
        except (json.JSONDecodeError, FileNotFoundError):
            user_data = {}

        user_data[self.user_name] = {
            "name": self.user_name,
            "task_list": self.task_list
        }
        with open(self.get_data_file_path(), 'w') as file:
            json.dump(user_data, file, indent=4)

y = tasks_manager("Yusuf")
y.edit_task()
