# Practice pass by function in Python
import math

def applyToEach(list, func):
    for i in range(len(list)):
        # Can think like casting
        list[i] = func(list[i])

def applyFuncs(listFunc, x):
    for func in listFunc:        
        print(func(x))      

listNum = [1, -3, 5.5]
# Print all absolute value
applyToEach(listNum, abs)
print(listNum)
# Print all int
applyToEach(listNum, int)
print(listNum)
# Print all factorial
applyToEach(listNum, math.factorial)
print(listNum)

# Assign the function into a list
listFunc = [abs, int, math.factorial]
applyFuncs(listFunc, 10)