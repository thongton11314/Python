import functools

#lambda arguments : expression
def valueMean(mylist):
    return functools.reduce(lambda a, b: a + b, mylist) / len(mylist) 

mylist = list(range(-10, 10))
print(list(filter(lambda a: a < 0, mylist)))
