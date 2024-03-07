foo = [1, 3, 4, 69, 71, 81, 90, 99, 420, 1337, 69420]


def binary_fn(haystack, needle):
    l_ptr, r_ptr = 0, len(haystack) - 1
    while l_ptr <= r_ptr:
        mid_ptr = (l_ptr + r_ptr) // 2
        if haystack[mid_ptr] > needle:
            r_ptr = mid_ptr - 1
        elif haystack[mid_ptr] < needle:
            l_ptr = mid_ptr + 1
        else:
            return True
    return False


print(binary_fn(foo, 69) is (True))
print(binary_fn(foo, 1336) is (False))
print(binary_fn(foo, 69420) is (True))
print(binary_fn(foo, 69421) is (False))
print(binary_fn(foo, 1) is (True))
print(binary_fn(foo, 0) is (False))
