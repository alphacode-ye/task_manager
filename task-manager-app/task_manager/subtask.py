# subtask.py

from task import tasks_manager

class SubTask(tasks_manager):
    def __init__(self, task_name, description, deadline, priority):
        super().__init__(task_name, description, deadline, priority)
        self.status = "In progress"
    
    def mark_complete(self):
        self.status = "Complete"
    


