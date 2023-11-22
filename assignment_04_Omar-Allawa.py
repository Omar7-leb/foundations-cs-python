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
          
      
           
      
            
