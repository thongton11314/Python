def doubleValue(arr):
    lst = []
    for each in arr:
        if arr.count(each) > 1 and each not in lst:
            lst.append(each)
    return lst
arr = [1,2, 45, 67, 45]
print(doubleValue(arr))