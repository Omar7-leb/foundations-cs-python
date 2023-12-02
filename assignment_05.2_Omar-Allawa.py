class Graph:
    def __init__(self):
        self.users = {}
        self.graph = []

    def add_user(self, username):
        if username in self.users:
            print(f"User already exists")
        else:
            self.users[username] = len(self.graph)
            for row in self.graph:
                row.append(0)
            self.graph.append([0] * (len(self.graph) + 1))
        return self
    
    def remove_user(self, username):
        
        if username not in self.users:
            print(f"User does not exist")
            return
        else:
            index = self.users[username]
            
            del self.users[username]
            
            del self.graph[index]
            
            for row in self.graph:
                del row[index]
                
            for key , value in self.users.items():
                if value > index:
                    self.users[key] = value - 1
    
    def send_friend_request(self , username1, username2):
        
        if username1 in self.users and username2 in self.users:
            index1 = self.users[username1]
            index2 = self.users[username2]
            
            self.graph[index1][index2] = 1
            self.graph[index2][index1] = 1
        
    def remove_friend(self , username1, username2):
        
        if username1 in self.users and username2 in self.users:
               index1 = self.users[username1]
               index2 = self.users[username2]
               
               self.graph[index1][index2] = 0
               self.graph[index2][index1] = 0
               
    def display_listoffriends(self):
        users = sorted(self.users.keys())
        matrix = [[0] * len(users) for _ in range(len(users))]

        for i, row in enumerate(self.graph):
           for j, value in enumerate(row):
               matrix[i][j] = value
               
        print("Connections:")
        for i, row in enumerate(matrix):
            print(users[i], " ".join(map(str, row)))
               
            
                         
    def displayusers(self):
        users = sorted(self.users.keys())
        matrix = [[0] * len(users) for _ in range(len(users))]

        for i, row in enumerate(self.graph):
           for j, value in enumerate(row):
               matrix[i][j] = value

        print("Users:")
        print(" ".join(users))
        
                
            

def main():
    socialmedia = Graph()
    print("Hello, there are a list of choices:")
    while True:
        user_input = int(input(" 1. Add a user to the platform.\n 2. Remove a user from the platform.\n 3. Send a friend request to another user.\n 4. Remove a friend from your list.\n 5. View your list of friends.\n 6. View the list of users on the platform.\n 7. Exit\n Please enter your choice here: "))
        if user_input == 1:
            username = input("Enter the username to add:")
            socialmedia.add_user(username)
            
        elif user_input == 2:
            username = input("Enter the username to remove:")
            socialmedia.remove_user(username)
            
        elif user_input == 3:
            username1 = input("Enter the 1st username : ")
            username2 = input("Enter the 2nd username : ")
            socialmedia.send_friend_request(username1, username2)
            
        elif user_input == 4:
            username1 = input("Enter the 1st username : ")
            username2 = input("Enter the 2nd username : ") 
            socialmedia.remove_friend(username1, username2)
            
        elif user_input == 5:
            socialmedia.display_listoffriends()
        
        elif user_input == 6:
            socialmedia.displayusers()
            
        elif user_input == 7:
            print("Exiting")
            break
            

if __name__ == "__main__":
    main()
