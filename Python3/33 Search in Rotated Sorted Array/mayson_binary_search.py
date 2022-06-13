from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def bin_search(nums, l, r, target):
            while l != r:
                m = l + (r - l) // 2
                if nums[m] == target:
                    return m
                if target > nums[m]:
                    if target >= nums[l] and nums[m] < nums[l]:
                        r = m
                    else:
                        l = m + 1
                else:
                    if target <= nums[r - 1] and nums[m] > nums[r - 1]:
                        l = m + 1
                    else:
                        r = m
            return -1

        return bin_search(nums, 0, len(nums), target)
