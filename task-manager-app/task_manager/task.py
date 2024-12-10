#task class task.py
import json
import time
import os
from datetime import datetime
from task_manager.user import User

class Tasks_manager(User):

    def __init__(self, user_name ) -> None:
        self.user_name = user_name
        self.task_priorityS = ("Red", "Yellow", "Green")
        self.target = None 
        self.subtask = []
    
    def get_data_file_path(self):
        return os.path.join(os.path.dirname(__file__), '..', 'data', 'data.json')
    
    def load_user_data(self):
        try:
            with open(self.get_data_file_path(), 'r+') as file:
                self.user_data = json.load(file)
                self.task_list = self.user_data.get(self.user_name, {}).get('task_list', {})
                for i in self.task_list.keys():
                    self.subtasks = self.user_data.get(self.user_name, {}).get('task_list', {}).get(i , {}).get('subtask' , [])
                    self.subtask.append(self.subtasks)
                return self.task_list
        except (json.JSONDecodeError, FileNotFoundError):
            self.user_data = {}
            self.task_list = {}
            self.subtasks = []
        
    
    def define_the_mission(self):
        view = User(self.user_name)
        self.load_user_data()
        try:
            if self.task_list:
                view.view_tasks()
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
            task_keys = [key for key in self.task_list[self.target] if key != "status" and key != "subtask" ]
            try:
                for index, key in enumerate(task_keys):
                    print(f"{index + 1}. {key}: **  {self.task_list[self.target][key]}  **")
                    time.sleep(0.50)
                edit_part = input("What do you want to change?[1.task name , 2.description , 3.deadline , 4.priority]\n")
                if edit_part.isdigit() and 1 <= int(edit_part) and int(edit_part) - 1 <= len(task_keys) and int(edit_part) != 4 and int(edit_part) != 3:
                    new_value = input("Write the new value\n")
                    self.task_list[self.target][str(task_keys[int(edit_part) - 1])] = new_value
                    # self.save_user_data()
                    print("Change done.\n")
                    return True
                elif int(edit_part) == 4:
                    priority = input("Enter task important [\u001b[31m1 = red,\u001b[33m 2 = yellow,\u001b[32m 3 = green\u001b[0m]\n")
                    self.task_list[self.target][str(task_keys[int(edit_part) - 1])] = self.task_priorityS[int(priority) - 1]
                    # self.save_user_data()
                    print("Change done.\n")
                elif int(edit_part) == 3:
                    while True:
                        user_input = input("enter didline(yyyy-mm-dd):\n")
                        try:
                            self.task_deadlien = datetime.strptime(user_input, "%Y-%m-%d" ).date()
                            if self.task_deadlien >= datetime.now().date():
                                self.task_list[self.target][str(task_keys[int(edit_part) - 1])] = f"{self.task_deadlien}"
                                print("Change done.\n")
                                break
                            else:
                                print("The task should not be in the past.")
                            pass
                        except:
                            print("You have entered the wrong format. It should be like (yyyy-mm-dd):")
                            pass
                else:
                    print("Invalid selection")
                    return "error"
            except ValueError:
                print("Invalid input")
                return "error"
        elif self.target is None:
            print("No task found to change")
            return "error"
        else:
            print("No task with this number")
            return "error"
        
    def mark_complete(self):
        self.define_the_mission()
        if self.target and self.target != "error":
            try:
                check = input("Are you done with this task?[1.yes , 2.No]\n")
                if check == "1":
                    self.task_list[self.target]["status"] = "Complete"
                    # self.save_user_data()
                    return "Complete"
                elif check == "2":
                    self.task_list[self.target]["status"] = "In progress"
                    # self.save_user_data()
                    return "In progress"
                else:
                    print("Invalid value Please choose 1 or 2")
                    return "error"
            except ValueError:
                print("Invalid input")
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
                    # self.save_user_data()
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
            file.close()

    
    def add_subtask(self, subtask1):
        self.define_the_mission()
        subtask1 = {subtask1:"In progress"}
        self.subtasks.append(subtask1)
        try:
            self.task_list[self.target]["subtask"].append(subtask1)
            # self.save_user_data()
            return subtask1
        except:
            self.task_list[self.target]["subtask"] = []
            self.task_list[self.target]["subtask"].append(subtask1)
            return subtask1

    
    def check_completion(self):
        for sub in self.task_list[self.target]["subtask"]:
            for s in (sub.values()):
                self.subtask.append(s)
        if all(subtask == "Complete" for subtask in self.subtask):
            self.task_list[self.target]["status"] = "Complete"
        return "Complete"


class Time_tracking():
    
    def __init__(self ,user_name):
        self.user_name = user_name
        self.task_list = {}
        self.time_spent = 0
        self.start_time = None
        
    
    def start_timer(self):
        if self.start_time is None:
            print("time track start")   
            self.start_time = time.time()
        else:
            print("tha time tracking is allredy start")
        return self.start_time
        
    
    def stop_timer(self):
        if self.start_time is not None:
            self.time_spent += time.time() - self.start_time
            self.start_time = None
            return self.time_spent
        
    
    def git_time_spent(self):
        mins, secs = divmod(int(self.time_spent), 60)
        timer = f"\033[1m{mins:02d}:{secs:02d}\033[0m"
        print(f"{timer} time spent in this task.")
        return f"{timer} time spent in this task."
        
    
    def reset_timer(self):
        self.time_spent = 0
        self.start_time = None
        return self.time_spent,self.start_time
        
    





