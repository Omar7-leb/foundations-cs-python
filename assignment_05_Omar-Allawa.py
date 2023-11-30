class Node:
    def __init__(self, name, family_name, birthdate):
        self.right = None
        self.left = None
        self.name = name
        self.family_name = family_name
        self.birthdate = birthdate

class Family_tree:
    def __init__(self):
        self.root = None

    def insert(self, name, family_name, birthdate):
        if self.root is None:
            self.root = Node(name, family_name, birthdate)
        else:
            current = self.root
            while current:
                if birthdate < current.birthdate:
                    if current.left is None:
                        current.left = Node(name, family_name, birthdate)
                        break
                    else:
                        current = current.left
                else:
                    if current.right is None:
                        current.right = Node(name, family_name, birthdate)
                        break
                    else:
                        current = current.right
            print("A family member added to the tree with name", name)

    def display_sorted_birthdays(self, node):
        if node is None:
            return

        self.display_sorted_birthdays(node.left)
        print(f"{node.name} {node.family_name}: {node.birthdate}")
        self.display_sorted_birthdays(node.right)

def main():
    member = Family_tree()
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

if __name__ == "__main__":
    main()
