from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        s = min_num = nums[0]
        for i in range(1, len(nums)):
            s += nums[i]
            min_num = min(min_num, nums[i])

        if s % 2 == 1 or n == 1:
            return False

        dp = [[False] * (s // 2 + 1) for _ in range(n)]  # [0, i] items sum to j

        if nums[0] <= s // 2:
            dp[0][nums[0]] = True
        for i in range(n):
            dp[i][0] = True  # empty set will sum to 0

        for i in range(1, n):
            for j in range(min_num, s // 2 + 1):
                if dp[i - 1][j] or (j >= nums[i] and dp[i - 1][j - nums[i]]):
                    dp[i][j] = True
        return dp[n - 1][s // 2]


# Optimized solution
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2 == 1:
            return False
        s = int(s / 2)

        dp = [False] * (s + 1)
        if nums[0] <= s:
            dp[nums[0]] = True
        dp[0] = True  # Empty set sum to 0

        for i in range(1, len(nums)):
            for j in reversed(range(1, s + 1)):
                if not dp[j] and j >= nums[i]:
                    dp[j] = dp[j - nums[i]]

        return dp[s]
