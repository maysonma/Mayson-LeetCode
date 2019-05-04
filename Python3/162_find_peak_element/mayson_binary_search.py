class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        def bin_search(nums, l, r):
            while l != r:
                m = l + (r - l) // 2
                if m == len(nums) - 1:
                    if nums[m] > nums[m - 1]:
                        return m
                    else:
                        r = m
                        continue
                if nums[m] > nums[m + 1]:
                    r = m
                else:
                    l = m + 1
            return l

        return bin_search(nums, 0, len(nums) - 1)
