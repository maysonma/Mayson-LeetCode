from collections import defaultdict
from heapq import heapify, heappop


class Solution:
    def frequencySort(self, s: str) -> str:
        f_dict = defaultdict(int)
        for char in s:
            f_dict[char] += 1
        max_heap = [(-v, k) for k, v in f_dict.items()]
        heapify(max_heap)
        ans = ""
        while max_heap:
            f, char = heappop(max_heap)
            ans += char * (-f)
        return ans