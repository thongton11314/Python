def smallestString(arr):
    key = arr[0]
    for each in arr:
        if len(key) > len(each) and len(key) != len(each):
            key = each  
    return key
arr = ["rose", "flower", "nice", "light", "beautiful", "ab", "ba"]
print(smallestString(arr)) 