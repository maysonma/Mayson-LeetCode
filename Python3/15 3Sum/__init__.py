class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        nums.sort()

        def two_sum(nums, target, start, triplets):
            l = start
            r = len(nums) - 1
            while l < r:
                if nums[l] + nums[r] == target:
                    triplets.append([-target, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                if nums[l] + nums[r] < target:
                    l += 1
                if nums[l] + nums[r] > target:
                    r -= 1

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            two_sum(nums, -nums[i], i + 1, triplets)
        return triplets
