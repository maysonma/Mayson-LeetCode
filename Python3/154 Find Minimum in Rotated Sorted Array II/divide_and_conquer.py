class Solution:
    def findMin(self, nums: List[int]) -> int:
        def find(nums, l, r):
            if l + 1 >= r:
                return min(nums[l:r + 1])
            if nums[l] < nums[r]:
                return nums[l]
            m = l + (r - l) // 2
            return min(find(nums, l, m), find(nums, m + 1, r))

        return find(nums, 0, len(nums) - 1)
