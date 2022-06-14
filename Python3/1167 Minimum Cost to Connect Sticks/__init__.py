from heapq import *
from typing import List


class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heapify(sticks)
        cost = 0
        while len(sticks) > 1:
            c = heappop(sticks)
            c += heappop(sticks)
            cost += c
            heappush(sticks, c)
        return cost
