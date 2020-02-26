import math
#List comprehension Practice

#Using map function, map(function, interator)
mypets = ["dog", "cat", "fish"]
myUpperPets = list(map(str.upper, mypets))
anotherPets = [pet.upper() for pet in mypets]
print(myUpperPets)
print(anotherPets)

number = [0.555, 0.355, 0.999, 0.445]
roundUpper = list(map(round, number))
print(roundUpper)

#Fun practice with iterator
def print_iterator(iter):
    for each in iter:
        print(each, end=' ')
    print('')  # for new line
map_iterator = map(str.upper, ['x', 'a', 'abc'])
print_iterator(map_iterator)

#Importing functools for reduce() 
import functools
numbers = [1, 1, 1, 1, 1, 5]
# reduce(function ,sequence) 
print(functools.reduce(lambda num1, num2: num1 + num2, numbers, 10))

