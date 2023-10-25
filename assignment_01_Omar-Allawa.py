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