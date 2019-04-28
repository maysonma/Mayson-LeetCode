class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def p(nums, d, m, used, curr, ans):
            if d == m:
                ans.append(curr[:])
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                used[i] = 1
                curr.append(nums[i])
                p(nums, d + 1, m, used, curr, ans)
                curr.pop()
                used[i] = 0

        ans = []
        used = [0] * len(nums)
        p(nums, 0, len(nums), used, [], ans)
        return ans
