from typing import List


class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        n = len(stones)
        if n == 1:
            return stones[0]

        total = sum(stones)
        s = total // 2

        dp = [[False] * (s + 1) for _ in range(n)]
        for i in range(n):
            dp[i][0] = True  # empty set sums to 0
        if stones[0] <= s:
            dp[0][stones[0]] = True

        for i in range(1, n):
            for j in range(1, s + 1):
                if dp[i - 1][j] or (j >= stones[i] and dp[i - 1][j - stones[i]]):
                    dp[i][j] = True

        for j in reversed(range(s + 1)):
            if dp[n - 1][j]:
                return total - 2 * j
