from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1
        if nums[end] >= nums[start]:
            return nums[0]
        while start < end:
            mid = start + (end - start) // 2
            if mid < end and nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            if mid > start and nums[mid] < nums[mid - 1]:
                return nums[mid]
            if nums[mid] >= nums[start]:  # left half sorted
                start = mid + 1
            else:
                end = mid - 1
