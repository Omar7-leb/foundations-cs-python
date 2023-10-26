#1
def CountDigits(number):
    counter = 0
    while number != 0:
        counter += 1
        number //= 10
        CountDigits(number)
    return counter