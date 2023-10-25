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