def smallestInt(arr):
    key = arr[0]
    for each in arr:
        if key > each: 
            key = each  
    return key
arr = [1, 5, 2, 4]
print(smallestInt(arr)) 