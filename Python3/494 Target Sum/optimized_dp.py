from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        """
        s1 - s2 = t
        s1 + s2 = s
        2 * s1 = t + s
        s1 = (t + s) / 2
        """
        n = len(nums)
        s = sum(nums)
        s1 = target + s
        if s < target or -s > target or s1 % 2 == 1:
            return 0
        else:
            s1 = int(s1 / 2)

        dp = [0] * (s1 + 1)
        dp[0] = 1
        if nums[0] <= s1:
            dp[nums[0]] += 1

        for i in range(1, n):
            for j in reversed(range(0, s1 + 1)):
                if j >= nums[i]:
                    dp[j] += dp[j - nums[i]]

        return dp[s1]
