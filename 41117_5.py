# 41117 - Udayan Chavan - P1
# Write a program for analysis of quick sort using deterministic and randomized variant

import random

# ------- Function to partition array with pivot = highest element
def partition(array, low, high):
    pivot = array[high]
    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])
            
    (array[i + 1], array[high]) = (array[high], array[i + 1])

    return i + 1

# ------- Function to partition array with pivot = random element
def partitionRandom(array, low, high):
    p = random.randrange(low, high)
    array[high], array[p] = array[p], array[high]

    return partition(array, low, high)

# ------- Function to run quick sort
def quickSort(array, low, high, r):
    if low < high:
        if r==1:
            p = partitionRandom(array, low, high)
        else:
            p = partition(array, low, high)

        quickSort(array, low, p-1, r)
        quickSort(array, p+1, high, r)

# ------------------------------------
A = [1, 7, 4, 1, 10, 9, -2]
size = len(A)
# ------------------------------------
print("Unsorted Array:", A)

r = int(input("Enter 0 - Fixed Pivot and 1 - Randomized Pivot: "))
quickSort(A, 0, size - 1, r)

print("Sorted Array:", A)