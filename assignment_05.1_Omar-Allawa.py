from graphviz import Digraph
class TreeNode:
    def __init__(self, name, family_name, birthdate):
        self.children = []
        self.name = name
        self.family_name = family_name
        self.birthdate = birthdate

class FamilyTree:
    def __init__(self):
        self.root = None
    
    def insert(self, name, family_name, birthdate):
        if self.root is None:
            self.root = TreeNode(name, family_name, birthdate)
        else:
            current = self.root
            current.children.append(TreeNode(name, family_name, birthdate))
            print("A family member added to the tree with name", name)
            
    def display_sorted_birthdays(self, node):
        if node is None:
            return

        for child in node.children:
            self.display_sorted_birthdays(child)
            
        print(f"{node.name} {node.family_name}: {node.birthdate}")
    
    
    def count_same_first_names(self, node, name):
        count = 0
        
        if node.name == name:
            count += 1

        for child in node.children:
            count += self.count_same_first_names(child, name)

        return count

def main():
    member = FamilyTree()
    print("Hello, there are a list of choices:")
    while True:
        user_input = int(input(
            "1. Add Family Member\n2. Display Sorted Birthdays\n3. Find Relationship\n4. Visualize Family Tree\n5. Count Same First Names\n6. Exit\nPlease enter your choice here: "))

        if user_input == 1:
            name = input("Enter the name you want to add: ")
            family_name = input("Enter the family name you want to add: ")
            birthdate = input("Enter the birthdate you want to add: ")
            member.insert(name, family_name, birthdate)

        elif user_input == 2:
            print("Sorted Birthdays:")
            member.display_sorted_birthdays(member.root)
            
            
        elif user_input == 5:
            first_name_to_count = input("Enter the first name to count: ")
            count = member.count_same_first_names(member.root, first_name_to_count)
            print(f"Number of family members with the same first name ({first_name_to_count}): {count}")
            
        elif user_input == 6:
            print("Exiting...")
            break

if __name__ == "__main__":
    main()
