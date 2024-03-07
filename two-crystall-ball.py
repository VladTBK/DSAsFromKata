import random
import math


def two_crystal_balls(arr):
    step = math.floor(math.sqrt(len(arr)))
    ptr = step
    try:
        while arr[ptr] is not True:
            ptr += step
    except IndexError:
        print("There were no True values")
        return -1
    for idx in range(ptr - step, ptr):
        if arr[idx] is True:
            return idx


runs = 10**6
idx = random.randint(0, runs)
data = [False for _ in range(runs)]

for i in range(idx, runs):
    data[i] = False

print(two_crystal_balls(data) is idx + 1)
