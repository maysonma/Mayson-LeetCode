# dp
from typing import List


class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        if n % 2 == 0:
            return True

        dp = [[[-1, -1] for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i][1] = nums[i]
            dp[i][i][0] = 0
        for l in range(1, n + 1):
            for i in range(n):
                j = i + l
                if j <= n - 1:
                    dp[i][j][1] = max(nums[i] + dp[i + 1][j][0], nums[j] + dp[i][j - 1][0])
                    dp[i][j][0] = min(dp[i + 1][j][1], dp[i][j - 1][1])
        print(dp[0][n - 1][1])
        return dp[0][n - 1][1] >= sum(nums) / 2
