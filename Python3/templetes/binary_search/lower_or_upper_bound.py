"""
return the lower_bound / upper_bound of a val in a sorted array
lower_bound(x): first index of i, such that A[i] >= x
upper_bound(x): first index of i, such that A[i] > x
core: Find the smallest index to satisfy g(index)
"""


def lower_bound(arr, val, l, r):
    m = l + (r - l) // 2
    while l != r:
        if arr[m] >= val:
            r = m
        else:
            l = m + 1
    return l


def upper_bound(arr, val, l, r):
    m = l + (r - l) // 2
    while l != r:
        if arr[m] > val:
            r = m
        else:
            l = m + 1
    return l
