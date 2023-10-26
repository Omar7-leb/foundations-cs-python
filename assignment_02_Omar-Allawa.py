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