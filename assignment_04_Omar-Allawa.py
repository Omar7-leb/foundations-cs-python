class Task:
     def __init__(self, task_id, description, priority , completed):
         self.task_id = task_id
         self.description = description
         self.priority = priority
         self.completed = completed
          
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
          self.completed = completed
      
           
      
            
