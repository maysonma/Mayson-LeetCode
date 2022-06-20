import random
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def find_kth_largest_rec(nums, start, end):
            nonlocal k, n
            p = partition(nums, start, end)
            if p == n - k:
                return nums[p]
            elif p < n - k:
                return find_kth_largest_rec(nums, p + 1, end)
            else:
                return find_kth_largest_rec(nums, start, p - 1)

        def partition(nums, start, end):
            pivot_idx = random.randint(start, end)
            nums[pivot_idx], nums[end] = nums[end], nums[pivot_idx]
            pivot = nums[end]

            for i in range(start, end):
                if nums[i] < pivot:
                    nums[i], nums[start] = nums[start], nums[i]
                    start += 1

            nums[start], nums[end] = nums[end], nums[start]
            return start

        n = len(nums)
        return find_kth_largest_rec(nums, 0, len(nums) - 1)
