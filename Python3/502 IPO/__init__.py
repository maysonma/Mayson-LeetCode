from heapq import *
from typing import List


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        min_capital_heap = []
        max_profit_heap = []
        cur_capital = w
        n = len(capital)

        for i in range(n):
            heappush(min_capital_heap, (capital[i], i))

        for _ in range(k):
            while len(min_capital_heap) > 0 and min_capital_heap[0][0] <= cur_capital:
                _, i = heappop(min_capital_heap)
                heappush(max_profit_heap, (-profits[i], i))

            if len(max_profit_heap) == 0:
                break

            cur_capital += -heappop(max_profit_heap)[0]

        return cur_capital
