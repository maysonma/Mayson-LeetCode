from collections import defaultdict
from heapq import heappush, heapreplace
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        f_dict = defaultdict(int)
        for num in nums:
            f_dict[num] += 1
        min_heap = []
        for num, f in f_dict.items():
            if len(min_heap) < k:
                heappush(min_heap, (f, num))
            elif f > min_heap[0][0]:
                heapreplace(min_heap, (f, num))
        return [num for _, num in min_heap]
