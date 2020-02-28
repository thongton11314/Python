import functools

# Testing lambda expression
# Result in lambda location in memory
print((lambda a,b: a + b))
# Result the lambda expression
print((lambda a,b: a + b)(1, 2))


mylist = list(range(-10, 10))

# Print number less than 10 by using fillter
# The filter() method filters the given sequence with the help of a function that tests each element in the sequence to be true or not
# filter(fun(), sequence) 
# Result in filter adress
print(filter(lambda a: a < 0, mylist))
# Result in list of element after filter 
print(list(filter(lambda a: a < 0, mylist)))

# Print the average by using reduce
# At first step, first two elements of sequence are picked and the result is obtained.
# Next step is to apply the same function to the previously attained result and the number just succeeding the second element and the result is again stored.
# This process continues till no more elements are left in the container.
# The final returned result is returned and printed on console. 
# reduce(fun(), sequence) 
print(functools.reduce(lambda a, b: a + b, mylist) / len(mylist))

