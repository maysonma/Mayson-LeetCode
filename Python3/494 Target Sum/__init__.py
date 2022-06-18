from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        s = sum(nums)
        if target > s or target < -s:
            return 0

        dp = [[0] * (2 * s + 1) for _ in range(n)]  # # ways to get target j from [0, i] nums
        dp[0][nums[0] + s] += 1
        dp[0][-nums[0] + s] += 1
        for i in range(1, n):
            for j in range(2 * s + 1):
                if j - nums[i] >= 0:
                    dp[i][j] += dp[i - 1][j - nums[i]]
                if j + nums[i] <= 2 * s:
                    dp[i][j] += dp[i - 1][j + nums[i]]

        return dp[n - 1][target + s]
