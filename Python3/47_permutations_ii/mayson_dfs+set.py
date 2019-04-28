class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        def p(nums, m, n, used, curr, ans):
            if m == n:
                ans.add(tuple(curr[:]))
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                used[i] = 1
                curr.append(nums[i])
                p(nums, m + 1, n, used, curr, ans)
                curr.pop()
                used[i] = 0

        ans = set([])
        used = [0] * len(nums)
        p(nums, 0, len(nums), used, [], ans)
        return list(ans)
