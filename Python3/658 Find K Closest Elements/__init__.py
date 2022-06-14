from heapq import *
from collections import deque
from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # binary search
        start = 0
        end = len(arr) - 1
        mid = 0
        while start <= end:
            mid = start + (end - start) // 2
            if arr[mid] == x:
                break
            elif x < arr[mid]:
                end = mid - 1
            else:
                start = mid + 1

        if arr[mid] == x:
            l, r = mid, mid + 1
        else:
            l, r = end, start

        ans = deque()
        while len(ans) < k:
            if r >= len(arr) or l >= 0 and (x - arr[l] <= arr[r] - x):
                ans.appendleft(arr[l])
                l -= 1
            else:
                ans.append(arr[r])
                r += 1
        return list(ans)
