from heapq import *
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []
        for num in nums:
            if len(min_heap) < k:
                heappush(min_heap, num)
            elif num > min_heap[0]:
                heappop(min_heap)
                heappush(min_heap, num)
            else:
                continue
        return min_heap[0]
