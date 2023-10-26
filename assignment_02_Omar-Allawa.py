#1
def CountDigits(number):
    number = abs(number)
    if number == 0:
        return 0
    else:
        return 1 + CountDigits(number // 10)

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

#3.2----------------------------------------------------------------
def mean(column):
    return sum(column) / len(column)

def standard_deviation(column):
    col_mean = mean(column)
    variance = sum((x - col_mean) ** 2 for x in column) / len(column)
    return variance ** 0.5

def is_normalized_column(column):
    return mean(column) == 0 and standard_deviation(column) == 1

def count_normalized_columns(matrix, column_idx=0):
    if column_idx >= len(matrix[0]):
        return 0

    column = [row[column_idx] for row in matrix]

    if is_normalized_column(column):
        return 1 + count_normalized_columns(matrix, column_idx + 1)
    else:
        return count_normalized_columns(matrix, column_idx + 1)
    

    
def main():
     user_input = input("Enter your choice : \n 1.Count Digits \n 2.Find Max \n 3.1.Count tags \n 3.2.Count Normalized Columns \n 4.Exit\n")
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
              
     elif user_input == "3.2":
         matrix = [
    [-1.2649110640673518, 5.123451, 43],
    [-0.6324555320336759, 5.13123123, 4334],
    [0.0, 6.1543453, 125879],
    [0.6324555320336759, 0.1231235709, 123544],
    [1.2649110640673518, 9.1543524234, 55676]
]

         normalized_column_count = count_normalized_columns(matrix)
         print(f"The number of normalized columns is: {normalized_column_count}")
      
     elif user_input == "4":
         return -1
         
     elif user_input == "3.1":
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