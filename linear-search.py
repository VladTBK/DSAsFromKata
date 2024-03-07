foo = [1, 3, 4, 69, 71, 81, 90, 99, 420, 1337, 69420, "hi mom"]


def linear_fn(haystack, needle):
    for val in haystack:
        if val == needle:
            return True
    return False


print(linear_fn(foo, 69) is (True))
print(linear_fn(foo, 1336) is (False))
print(linear_fn(foo, 69420) is (True))
print(linear_fn(foo, 69421) is (False))
print(linear_fn(foo, 1) is (True))
print(linear_fn(foo, 0) is (False))
print(linear_fn(foo, "hi mom") is (True))
