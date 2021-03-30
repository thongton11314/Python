#list comprehension work as: [Return from condition ... Condition Statement]
#lambda work as: lambda arguments : expression

#Style of newbie
def square():
    result = []
    for a in range(1,30):
        for b in range(1,30):
            for c in range(1,30):
                if (a**2 + b**2 == c**2):
                    result.append((a,b,c))
    return result

#Style of immediate
def isSquare(a,b,c):
        return a**2 + b**2 == c**2

def square2():    
    return [(a,b,c) for a in range(1,30) for b in range(1,30) for c in range(1,30) if isSquare(a,b,c)]

#Style of legendary
def square3():    
    return [(a,b,c) for a in range(1,30) for b in range(1,30) for c in range(1,30) if a**2 + b**2 == c**2]

#Style of noob
def square4():
    return [(lambda a,b,c: (a,b,c))(a,b,c) for a in range(1,30) for b in range(1,30) for c in range(1,30) if a**2 + b**2 == c**2]

print("They are all the same" if square() == square2() == square3() == square4() else "Not the same")