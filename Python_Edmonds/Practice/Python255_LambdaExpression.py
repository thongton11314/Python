def isEven(item):
    return True if item % 2 == 0 else False

#Lamda expression
isEven2 = lambda item: item % 2 == 0
print(isEven(10))
print(isEven2(10))
print((lambda item: item % 2 == 0)(10))

#Lambda expression 1
lst = [1, 2, 3, 4, 5]
lst1 = [(lambda x: x * 2)(x) for x in lst]
print(lst1)