#1------------------------------------------------------------
def factorial(n):
    if n < 0:
        print("Give a positive number!")
        return None
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

while True:
    user_input = int(input("Enter a positive number: "))
    result = factorial(user_input)
    if result is not None:
        print("Factorial of " + f"{user_input} is {result}")
        
#2------------------------------------------------------------
def divisors(n):
    list = []
    for i in range(1, n+1):
        if n % i == 0:
            list.append(i)
    return list
while True:
    user_input = int(input("Enter a positive number"))
    result = divisors(user_input)
    print(f"Divisors of {user_input}: {result}")
    

#3--------------------------------------------------------
def reverse(word):
    reverse = ""
    for i in range(len(word)-1, -1, -1):
        reverse += word[i]
    return reverse
while True:   
    user_input = input("Give a word to reverse it : ")
    result = reverse(user_input)
    print("the reverse of " + user_input + " is : " + result) 
    
#4----------------------------------------------------------
def Evennumber(input_list):
    even_numbers = []
    for i in input_list:
        if i % 2 == 0:
            even_numbers.append(i)
    return even_numbers

list_length = int(input('Give the length of the list: '))
user_list = []
for i in range(list_length):
    user_input = int(input("Enter a number: "))
    user_list.append(user_input)
result = Evennumber(user_list)
print(user_list)
print(result)

#5--------------------------------------------------------
def Password(password):
    length_condition = len(password) >= 8
    uppercase_condition = False
    lowercase_condition = False
    digit_condition = False
    special_condition = False
    
    for char in password:
        if char.isupper():
            uppercase_condition = True
        elif char.islower():
            lowercase_condition = True
        elif char.isdigit():
            digit_condition = True
        elif char in '#?!$':
            special_condition = True

    if length_condition and uppercase_condition and lowercase_condition and digit_condition and special_condition:
        return "Strong Password"
    else:
        return "Weak Password"
while True:
    password = input("Give me a password: ")
    result = Password(password)
    print(result)
    
#6----------------------------------------------------------------
def Ipv4(ipv4):
    parts = ipv4.split('.')
    
    if len(parts) != 4:
        return False
    else:
        for part in parts:
           num = int(part)
           
           if num <0 or num > 255:
               return False
    return True

while True:
    user_input =input("Give me an Ipv4 address:")
    if Ipv4(user_input):
        print(f"{user_input} is a valid IPv4 address")
    else:
        print(f"{user_input} is not a valid IPv4 address")

#7------------------------------------------------------------
#Mean
def Mean(list):
    total_sum = 0
    for i in list:
        total_sum += i
    mean = total_sum / len(list)
    return mean
#Median
def Median(list):
    sorted_numbers = sorted(list)
    n = len(sorted_numbers)
    if n % 2 == 1:
        return sorted_numbers[n // 2]
    else:
        mid1 = sorted_numbers[(n - 1) // 2]
        mid2 = sorted_numbers[n // 2]
        return (mid1 + mid2) / 2
#Mode       
def Mode(list):
    if len(list) == 0:
        return "No mode"
    
    list.sort()  
    max_count = 1  
    current_count = 1  
    mode = [list[0]]  

    for i in range(1, len(list)):
        if list[i] == list[i - 1]:
            current_count += 1
        else:
            if current_count > max_count:
                max_count = current_count
                mode = [list[i - 1]]
            elif current_count == max_count:
                mode.append(list[i - 1])
            current_count = 1
            
    if current_count > max_count:
        mode = [list[-1]]
    elif current_count == max_count:
        mode.append(list[-1])

    if max_count == 1:
        return "No mode"
    
    return mode

#Range
def rangeNb(list):
    if len(list) == 0 :
        return 0
    min = list[0]
    max = list[0]
    for i in range(1,len(list)):
        if list[i] < min:
            min = list[i]
    
        if list[i] > max:
            max = list[i]
        
    return max - min

#Variance
def Variance(list):
    mean = Mean(list)
    sum_squared_diff = 0
    n = len(list)
    
    for x in list:
        sum_squared_diff += (x - mean) ** 2

    variance = sum_squared_diff / n
    return variance

#Standart Deviation
def Standart_Deviation(list):
    variance = Variance(list)
    sd = variance ** 0.5
    return sd


user_list = []

while True:
    user_input = input("Enter a number (or type 'done' to finish): ")

    if user_input == 'done':
        break

    if user_input.isdigit():
        num = int(user_input)
        user_list.append(num)
    else:
        print("Invalid input. Please enter a valid number.")

if user_list: 
    mean = Mean(user_list)
    median = Median(user_list)
    mode = Mode(user_list)
    rangeNb = rangeNb(user_list)
    variance = Variance(user_list)
    sd = Standart_Deviation(user_list)
    print("Your list:", user_list)
    print("Mean:", mean)
    print("Median",median)
    print("Mode:", mode)
    print("Range:", rangeNb)
    print("variance:", variance)
    print("Standard_Deviation:", sd)
else:
    print("The list is empty.")
