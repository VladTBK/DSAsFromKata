import random
import sys

sys.setrecursionlimit(10**6)


def partition(array, low, high):
    # choose the rightmost element as pivot
    pivot = array[high]

    # pointer for greater element
    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1

            (array[i], array[j]) = (array[j], array[i])

    (array[i + 1], array[high]) = (array[high], array[i + 1])

    return i + 1


# function to perform quicksort


def quick_sort(array, low, high):
    if low < high:
        # Find pivot element such that
        pi = partition(array, low, high)

        quick_sort(array, low, pi - 1)
        quick_sort(array, pi + 1, high)


arr = [random.randint(0, 10**2) for _ in range(10**1)]
print(arr)
quick_sort(arr, 0, len(arr) - 1)
print(arr)
