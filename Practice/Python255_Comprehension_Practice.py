#Working with list
lst = [1,2,3,4]
cubic_list = [item**3 for item in lst if item % 2 == 0]
print(cubic_list)

#Working with string
movies = ['A movie', 'F movie', 'D movie', 'E movie', 'C movie', 'B movie']
startwithMovie = [title for title in movies if title.startswith("A")]
print(startwithMovie)

#Working with tuple
movies1 = [('A movie', 2000), ('F movie', 2006), ('D movie', 2004), ('E movie', 2005), ('C movie', 2003), ('B movie', 2002)]
pre2k5 = [(title, year) for (title, year) in movies1 if year < 2005] 
print(pre2k5)

#Working with cartesian product
A = [1, 2, 3] 
B = [-1,-2,-3]
cartasian = [(a, b) for a in A for b in B]
print(cartasian)
