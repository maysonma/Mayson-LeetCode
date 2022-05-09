from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p1 = p2 = 0
        while p2 < len(nums):
            if nums[p2] > nums[p1]:
                p1 += 1
                nums[p1] = nums[p2]
            p2 += 1
        return p1 + 1
