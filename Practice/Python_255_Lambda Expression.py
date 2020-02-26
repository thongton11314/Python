def isEven(item):
    return True if item % 2 == 0 else False

isEven2 = lambda item: item % 2 == 0
print(isEven(10))
print(isEven2(10))
print((lambda item: item % 2 == 0)(10))
