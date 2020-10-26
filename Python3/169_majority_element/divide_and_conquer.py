class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        def major(nums, l, r):
            if l == r:
                return nums[l]
            m = l + (r - l) // 2
            ml = major(nums, l, m)
            mr = major(nums, m + 1, r)
            if ml == mr:
                return ml
            else:
                return ml if nums[l:r + 1].count(ml) > nums[l:r + 1].count(mr) else mr

        return major(nums, 0, len(nums) - 1)
