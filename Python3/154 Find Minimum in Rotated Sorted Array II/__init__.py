from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1
        while start < end:
            mid = start + (end - start) // 2
            if start < mid and nums[mid - 1] > nums[mid]:
                return nums[mid]
            if mid < end and nums[mid] > nums[mid + 1]:
                return nums[mid + 1]

            if nums[mid] == nums[start] == nums[end]:
                if nums[start] > nums[start + 1]:
                    return nums[start + 1]
                start += 1
                if nums[end - 1] > nums[end]:
                    return nums[end]
                end -= 1
            elif nums[mid] > nums[start] or \
                    (nums[mid] == nums[start] and nums[mid] > nums[end]):
                start = mid + 1
            else:
                end = mid - 1
        return nums[0]
