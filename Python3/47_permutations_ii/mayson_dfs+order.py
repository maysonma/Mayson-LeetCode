class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        def p(nums, m, n, used, curr, ans):
            if m == n:
                ans.append(curr[:])
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue
                used[i] = 1
                curr.append(nums[i])
                p(nums, m + 1, n, used, curr, ans)
                curr.pop()
                used[i] = 0

        ans = []
        used = [0] * len(nums)
        p(nums, 0, len(nums), used, [], ans)
        return list(ans)
