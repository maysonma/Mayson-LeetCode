class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        ans = 0
        prod = 1
        l = 0
        for r in range(len(nums)):
            if nums[r] >= k:
                prod = k
                continue
            if prod * nums[r] < k:
                prod *= nums[r]
            else:
                l = r
                prod = nums[r]
            while l > 0:
                if prod * nums[l - 1] < k:
                    l -= 1
                    prod *= nums[l]
                else:
                    break
            ans += (r - l + 1)
        return ans
