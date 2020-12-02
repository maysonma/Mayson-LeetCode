from typing import List


class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        n = len(sticks)
        sticks.sort()
        internals = [0] * n
        i = j = 0
        k = -1

        def getmin():
            nonlocal i, j
            if j > k or i < n and sticks[i] < internals[j]:
                i += 1
                return sticks[i - 1]
            else:
                j += 1
                return internals[j - 1]

        while k != n - 2:
            a = getmin()
            b = getmin()
            k += 1
            internals[k] = a + b
        return sum(internals[:n - 1])
