"""
Templete: [l, r)
"""


def binary_search(l, r):
    def f(m):
        return True  # if arr[m] == target

    def g(m):
        return True  # if target is in the left

    while l != r:
        m = l + (r - l) // 2
        if f(m):
            return m
        if g(m):
            r = m  # new range [l, m)
        else:
            l = m + 1  # new range [m+1, r)
    return l  # or not found


def bin_search(arr, target, l, r):
    while l != r:
        m = l + (r - l) // 2
        if arr[m] == target:
            return m
        if arr[m] > target:
            r = m
        else:
            l = m + 1
    return -1


input0 = [1, 2, 5, 6, 7, 8, 12]
r1 = bin_search(input0, 8, 0, len(input0))
r2 = bin_search(input0, 6, 0, len(input0))
print(r1, r2)
