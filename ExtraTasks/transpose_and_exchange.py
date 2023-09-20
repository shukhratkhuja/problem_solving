import math
import random

n = int(input("Massiv elementlari sonini kiriting: "))

arr = [random.randint(0, 100) for _ in range(n)]
print("Massiv elementlari: ", arr)

def partition(array, low, high):

    pivot = array[high]
    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1

def transpositioning(array, low, high):
    if low < high:

        pi = partition(array, low, high)
        transpositioning(array, low, pi - 1)
        transpositioning(array, pi + 1, high)

transpositioning(arr, 0, len(arr) - 1)
print(f'Min element: {arr[0]}')
