class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def lower_bound(arr, val, l, r):
            while l != r:
                m = l + (r - l) // 2
                if arr[m] >= val:
                    r = m
                else:
                    l = m + 1
            return l
        def upper_bound(arr, val, l, r):
            while l != r:
                m = l + (r - l) // 2
                if arr[m] > val:
                    r = m
                else:
                    l = m + 1
            return l
        left = lower_bound(nums, target, 0, len(nums))
        if left == len(nums) or nums[left] != target:
            return [-1, -1]
        else:
            right = upper_bound(nums, target, 0, len(nums))
            return [left, right - 1]