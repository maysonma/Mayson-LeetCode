class Solution:
    def findMin(self, nums: List[int]) -> int:
        def find(nums, l, r):
            if nums[l] < nums[r]:
                return nums[l]
            if l + 1 >= r:
                return min(nums[l:r + 1])
            m = l + (r - l) // 2
            return min(find(nums, l, m - 1), find(nums, m, r))

        return find(nums, 0, len(nums) - 1)
