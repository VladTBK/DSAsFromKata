import random

arr = [random.randint(0, 10**3) for _ in range(10**1)]


def bubble_sort(arr):
    arr_len = len(arr)
    for i in range(arr_len):
        for j in range(arr_len - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j + 1], arr[j] = arr[j], arr[j + 1]


print(arr)
bubble_sort(arr)
print(arr)
