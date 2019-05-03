class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        sigma = sum(nums)
        target, r = divmod(sigma, k)
        if r != 0:
            return False
        nums.sort(reverse=True)
        n = k
        s = 0
        while s < len(nums):
            if nums[s] < target:
                break
            elif nums[s] > target:
                return False
            else:
                n -= 1
            s += 1
        bins = [target] * n

        # remain = target * n
        def search(nums, s, bins, remain):
            if remain == 0:
                return True
            for i in range(len(bins)):
                if nums[s] <= bins[i]:
                    bins[i] -= nums[s]
                    if search(nums, s + 1, bins, remain - nums[s]):
                        return True
                    bins[i] += nums[s]
            return False

        return search(nums, s, bins, target * n)
