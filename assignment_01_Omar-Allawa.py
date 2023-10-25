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
