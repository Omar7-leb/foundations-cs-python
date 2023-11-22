class Task:
    task_id = 0
    def __init__(self, description, priority , completed):
         Task.task_id += 1
         self.description = description
         self.priority = priority
         self.completed = completed
         
    def get_task_id(self):
        return self.task_id
          
    def get_descriptions(self):
           return  self.description
        
    def set_descriptions(self, description):
         self.description = description
      
    def get_priority(self):
           return self.priority
      
    def set_priority(self, priority):
         self.priority = priority
        
    def get_completed(self):
          return  self.completed
          
    def set_completed(self, completed):
          self.completed = True
          
      
class Node:
    def __init__(self, task):
        self.task = task
        self.next = None    
        
class PriorityQueue:
    def __init__(self):
        self.header = None
        self.size = 0       
        
    def isEmpty(self):
        return self.header == None
    
    def displayQueue(self):
        current = self.header
        
        while(current.next != None):
            print(f"The id of task :{current.task.get_id()}, Priority :{current.task.get_priority()}, Description :{current.task.get_description()}")
            current = current.next
            
        
        
        
      
            
