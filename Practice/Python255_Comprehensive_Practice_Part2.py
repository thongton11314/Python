def square():
    result = []
    for a in range(1,30):
        for b in range(1,30):
            for c in range(1,30):
                if (a**2 + b**2 == c**2):
                    result.append((a,b,c))
    return result

def square2():
    #Return from condition ... For loop ... Condition Statement
    return [(a,b,c) for a in range(1,30) for b in range(1,30) for c in range(1,30) if a**2 + b**2 == c**2]


def isSquare(a,b,c):
        return a**2 + b**2 == c**2

def square3():    
    return [(a,b,c) for a in range(1,30) for b in range(1,30) for c in range(1,30) if isSquare(a,b,c)]



print(square())
print(square2())
print(square3())