#List comprehension
mypets = ["dog", "cat", "fish"]
myUpperPets = list(map(str.upper, mypets))
anotherPets = [pet.upper() for pet in mypets]
print(myUpperPets)
print(anotherPets)