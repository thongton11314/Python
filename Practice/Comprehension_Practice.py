list = [1,2,3,4]

#It is the same as 
#for item in lst:
#    if item % 2 == 0:
#        item = item**3

cubic_list = [item**3 for item in list if item % 2 == 0]
print(cubic_list)
