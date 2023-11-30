class Node:
    def __init__(self , name , family_name , birthdate):
        self.right = None
        self.left = None
        self.name = name
        self.family_name = family_name
        self.birthdate = birthdate
        
class Family_tree:
    
    def __init__(self):
        self.root = None
        
    def insert(self , name , family_name , birthdate):
        if (self.root == None):
            self.root = Node(name, family_name, birthdate)
            
        else:
            current = self.root
            
            while (current != None):
                if birthdate < current.birthdate:
                    if current.left == None:
                        current.left = Node(name, family_name, birthdate)
                        current = None
                    else:
                        current = current.left
                else:
                    if current.right == None:
                        current.right = Node(name, family_name, birthdate)
                        current = None
                    else:
                        current = current.right
            print("A family member added to the tree with name" , name)
        

def main():
    print ("Hello , there are a list of choices:")
    user_input = int(input(" 1. Add Family Member\n 2. Display Sorted Birthdays\n 3. Find Relationship\n 4. Visualize Family Tree\n 5. Count Same First Names\n 6. Exit\n please enter you choice here : "))
    
    if user_input == 1:
       name = input("Enter the name you want to add : ") 
       family_name = input("Enter the family name you want to add : ")
       birthdate = input("Enter the birthdate you want to add : ")
       member = Family_tree()
       member.insert(name , family_name , birthdate)
if __name__ == "__main__":
    main()
   