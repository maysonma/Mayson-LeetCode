from heapq import *
from typing import List


class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        ans = [-1] * n

        min_end_heap = []
        min_start_heap = []
        for i in range(n):
            intv = intervals[i]
            heappush(min_start_heap, (intv[0], i))
            heappush(min_end_heap, (intv[1], i))

        while min_end_heap:
            end, i = heappop(min_end_heap)
            while min_start_heap and min_start_heap[0][0] < end:
                heappop(min_start_heap)
            if not min_start_heap:
                break
            ans[i] = min_start_heap[0][1]
        return ans
