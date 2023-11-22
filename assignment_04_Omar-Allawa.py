class Task:
    task_id = 0
    def __init__(self, description, priority , completed = False):
         Task.task_id += 1
         self.task_id = Task.task_id
         self.description = description
         self.priority = priority
         self.completed = completed
         
    def get_task_id(self):
        return self.task_id
          
    def get_description(self):
           return  self.description
        
    def set_description(self, description):
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
        Task.task_id = 0
        self.header = None
        self.size = 0       
        
    def isEmpty(self):
        return self.header == None
    
    def displayQueue(self):
        current = self.header

        while current is not None:
            print(f"The id of task: {current.task.get_task_id()}, Priority: {current.task.get_priority()}, Description: {current.task.get_description()}")
            current = current.next
            
    def enqueue(self, task):
        node = Node(task)
        
        if self.isEmpty() or task.get_priority() > self.header.task.get_priority():
            node.next = self.header
            self.header = node
            
        else:
            current = self.header
            
            while current.next != None and task.get_priority() <=current.next.task.get_priority():
               current = current.next
               
            node.next = current.next
            current.next = node 

           
            
        
        
      
            
