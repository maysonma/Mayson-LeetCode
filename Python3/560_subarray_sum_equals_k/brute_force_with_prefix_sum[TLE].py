class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if not n:
            return 0
        sum_arr = [0] * n
        sum_arr[0] = nums[0]
        for i in range(1, n):
            sum_arr[i] = sum_arr[i-1] + nums[i]
        ans = 0
        for i in range(n):
            for j in range(i+1, n):
                if sum_arr[j] - sum_arr[i] == k:
                    ans += 1
        for i in range(n):
            if sum_arr[i] == k:
                ans += 1
        return ans