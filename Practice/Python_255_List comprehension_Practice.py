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