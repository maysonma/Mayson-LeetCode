class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum_dict = {0: 1}
        cur_sum = 0
        ans = 0
        n = len(nums)
        for i in range(n):
            cur_sum += nums[i]
            ans += prefix_sum_dict.get(cur_sum - k, 0)
            prefix_sum_dict[cur_sum] = prefix_sum_dict.get(cur_sum, 0) + 1
        return ans
