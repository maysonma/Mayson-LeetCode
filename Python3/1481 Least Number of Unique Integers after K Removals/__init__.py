from collections import defaultdict
from heapq import heapify, heappop
from typing import List


class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        freq_dict = defaultdict(int)
        for num in arr:
            freq_dict[num] += 1

        count = len(freq_dict)
        min_heap = [(f, num) for num, f in freq_dict.items()]
        heapify(min_heap)
        while k > 0:
            f, num = heappop(min_heap)
            k -= f
            if k >= 0:
                count -= 1
        return count
