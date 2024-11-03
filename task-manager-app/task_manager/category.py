from abc import ABC,abstractmethod

class taskcategory(ABC):
    
    def __init__(self, title, description, deadline, priority ):
        self.title = title
        self.description = description
        self.deadline = deadline
        self.priority = priority
        
    
    @abstractmethod
    def task_info(self):
        pass
    
    @abstractmethod
    def set_priority(self, priority):
        pass


class WorkTask(taskcategory):
    
    def task_info(self):
        return f"Work Task: {self.title}\n Description: {self.description}\n Deadline: {self.deadline}\n Priority: {self.priority}"
    
    def set_priority(self, priority):
        self.priority = priority
        return f"Priority set to {self.priority} for work task: {self.title}"
    


class PersonalTask(taskcategory):
    
    def task_info(self):
        return f"Personal Task: {self.title}\n Description: {self.description}\n Deadline: {self.deadline}\n Priority: {self.priority}"
    
    def set_priority(self, priority):
        self.priority = priority
        return f"Priority set to {self.priority} for personal task: {self.title}"


class StudyTask (taskcategory):
    def task_info(self):
        return f"Study Task: {self.title}\n Description: {self.description}\n Deadline: {self.deadline}\n Priority: {self.priority}"
    
    def set_priority(self, priority):
        self.priority = priority
        return f"Priority set to {self.priority} for study task: {self.title}"








