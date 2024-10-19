import json
import user
import time


class tasks_manger(user.user1):
    
    def __init__(self , user_name) -> None:
        self.user_name = user_name
        self.target = None
        self.load_user_data()
    
    def load_user_data(self):
        try:
            with open('data\\data.json', 'r') as file:
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
                all_tasks =[] 
                for i in self.task_list:
                    all_tasks.append(i)
                target_namber = int(input("Enter the task number:\n"))
                self.target = all_tasks[target_namber - 1]
                return self.target
            else:
                self.target = None
                return None
        except (IndexError , ValueError):
            self.target = True
            return "error"  
        
    
    def edit_task(self):
        self.define_the_mission()
        task_splet = []
        if self.target !=True and self.target != None:
            for i in self.task_list[self.target]:
                if i != "status":
                    task_splet.append(i)
                    print(i + ":\n          " + "**" + self.task_list[self.target][i] + "**" )
                    time.sleep(1)
                else:
                    pass
            edit_part = int(input("What do you want to change?[1.description , 2.deadline , 3.priority]\n"))
            self.task_list[self.target][task_splet[edit_part - 1]] = input("Write the new value\n")
            self.save_user_data()
            print("change done")
            return True
        elif self.target == None :
            print("No task found to change")
            return False
        else:
            print("no task with this number.")
            return "error"
        
    
    def mark_complete(self):
        self.define_the_mission()
        if self.target !=True and self.target != None:
            chack = int(input("Are you done with this task?[1.yes , 2.No]\n"))
            if chack == 1:
                self.task_list[self.target]["status"] = "Complete"
                self.save_user_data()
                return "Complete"
            elif chack == 2:
                self.task_list[self.target]["status"] = "In progress"
                self.save_user_data()
                return "In progress"
            else:
                print("Invalid value. Please try again and choose one of the two numbers.")
                pass
        else:
            print("No task found")
            return False
        
        
    
    def delete_task(self):
        self.define_the_mission()
        if self.target !=True and self.target != None:
            sure = int(input("Are you sure you want to delete this task?[1.yes , 2.No]\n"))
            if sure == 1:
                del self.task_list[self.target]
                self.save_user_data()
                print("done")
                return "done"
            elif sure == 2:
                return "In progress"
            else:
                print("Invalid value. Please try again and choose one of the two numbers.")
                return "error"
        else:
            print("No task found")
            return False
    




