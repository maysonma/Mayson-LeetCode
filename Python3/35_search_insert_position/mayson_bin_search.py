class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        def bin_search(arr, val, l, r):
            while l != r:
                m = l + (r - l) // 2
                if arr[m] == val:
                    return m
                if arr[m] > val:
                    r = m
                else:
                    l = m + 1
            return l
        return bin_search(nums, target, 0, len(nums))