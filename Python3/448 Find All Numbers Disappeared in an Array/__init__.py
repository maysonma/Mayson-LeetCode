from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        i, n = 0, len(nums)
        while i < n:
            j = nums[i] - 1
            if i != j and nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1
        ans = []
        for i in range(n):
            if nums[i] != i + 1:
                ans.append(i + 1)
        return ans
