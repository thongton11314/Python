def searchKeyWord(arr, keyWord):
    lst = []
    for each in arr:
        if keyWord in each:
            lst.append(each)
    return lst
arr = ["rose", "flower", "nice", "light", "beautiful"]
print(searchKeyWord(arr, 'e'))