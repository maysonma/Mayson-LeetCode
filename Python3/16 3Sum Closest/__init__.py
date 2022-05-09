class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        min_diff = target - sum(nums[:3])
        nums.sort()

        for i in range(len(nums)):
            if min_diff == 0:
                return target

            l = i + 1
            r = len(nums) - 1
            while l < r:
                curr_sum = nums[i] + nums[l] + nums[r]
                curr_diff = target - curr_sum
                if abs(curr_diff) < abs(min_diff):
                    min_diff = curr_diff
                if curr_diff > 0:
                    l += 1
                else:
                    r -= 1
        return target - min_diff


