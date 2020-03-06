import random

def randomSwapIntegerList(arr):
    for i in range(len(arr)):
        pivot = random.randint(0, len(arr) - 1)
        temp = arr[i]
        arr[i] = arr[pivot]
        arr[pivot] = temp
    return arr

lst = [1, 2, 3, 4, 5]
print(randomSwapIntegerList(lst.copy()))