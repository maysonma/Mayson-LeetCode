from heapq import *
from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        min_heap = [(matrix[i][0], 0, matrix[i]) for i in range(min(k, n))]
        heapify(min_heap)
        count = 0
        num = None
        while min_heap:
            num, idx, row = heappop(min_heap)
            count += 1
            if count == k:
                break
            if idx + 1 < len(row):
                heappush(min_heap, (row[idx + 1], idx + 1, row))
        return num
