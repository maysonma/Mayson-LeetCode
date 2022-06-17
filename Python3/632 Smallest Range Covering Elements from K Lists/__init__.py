from heapq import *
from typing import List


class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        min_heap = [(l[0], 0, l) for l in nums]
        heapify(min_heap)
        max_num = max(min_heap)[0]
        min_range = [min_heap[0][0], max_num]
        min_range_len = min_range[1] - min_range[0]
        while min_heap:
            num, idx, l = heappop(min_heap)
            if idx + 1 < len(l):
                max_num = max(l[idx + 1], max_num)
                heappush(min_heap, (l[idx + 1], idx + 1, l))
                if max_num - min_heap[0][0] < min_range_len:
                    min_range = [min_heap[0][0], max_num]
                    min_range_len = min_range[1] - min_range[0]
            else:
                return min_range
