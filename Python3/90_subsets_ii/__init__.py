from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        nums.sort()
        start = 0
        end = 1

        for i in range(len(nums)):
            start = 0
            if i > 0 and nums[i] == nums[i - 1]:
                start = end
            end = len(ans)
            for j in range(start, end):
                ss = list(ans[j])
                ss.append(nums[i])
                ans.append(ss)
        return ans
