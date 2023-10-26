#1
def CountDigits(number):
    counter = 0
    while number != 0:
        counter += 1
        number //= 10
        CountDigits(number)
    return counter

#2--------------------------------
def FindMax(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        max_rest = FindMax(lst[1:])
        return max_rest if max_rest > lst[0] else lst[0]
    
#3.1--------------------------------
def count_tag_occurrences(html, tag):
    start_tag = f"<{tag}>"
    end_tag = f"</{tag}>"
    
    start_index = html.find(start_tag)
    
    if start_index == -1:
        return 0
    
    open_tags = 0
    for index in range(start_index, len(html)):
        if html[index:index + len(start_tag)] == start_tag:
            open_tags += 1
        elif html[index:index + len(end_tag)] == end_tag:
            open_tags -= 1

            
            if open_tags == 0:
                end_index = index + len(end_tag)
                break
            
    remaining_html = html[end_index:]
    return 1 + count_tag_occurrences(remaining_html, tag)



        

def main():
     user_input = input("Enter your choice : \n 1.Count Digits \n 2.Find Max \n 3.1. Count tags \n 4.Exit\n")
     if user_input == "1":
         number = int(input("Enter a number : "))
         digit_count = CountDigits(number)
         print("Number of digits:", digit_count)
    
     elif user_input == "2":
         user_list = []
         while True:
           element = input("Enter a number or 'End' to finish: ")
        
           if element == 'End':
              break  
    
           num = int(element)
           user_list.append(num)
        
         if user_list:
            max_value = FindMax(user_list)
            print("The maximum value in the list is:", max_value)
         else:
              print("The list is empty.")
              
     elif user_input == "3":
         html = """
<html>
<head>
<title>My Website</title>
</head>
<body>
<h1>Welcome to my website!</h1>
<p>Here you'll find information about me and my hobbies.</p>
<h2>Hobbies</h2>
<ul>
<li>Playing guitar</li>
<li>Reading books</li>
<li>Traveling</li>
<li>Writing cool h1 tags</li>
</ul>
</body>
</html>
"""

# Get the tag from the user
     tag_to_count = input("Enter the HTML tag to count: ")

# Call the function to count tag occurrences
     occurrences = count_tag_occurrences(html, tag_to_count)
     print(f"The '{tag_to_count}' tag occurs {occurrences} times in the HTML code.")

         
         
        
        
     
         
if __name__ == "__main__":
    main()