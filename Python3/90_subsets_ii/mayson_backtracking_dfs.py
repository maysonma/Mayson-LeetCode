class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        def dfs(nums, s, cur, ans):
            ans.append(cur[:])
            for i in range(s, len(nums)):
                if i > s and nums[i] == nums[i - 1]:
                    continue
                cur.append(nums[i])
                dfs(nums, i + 1, cur, ans)
                cur.pop()

        ans = []
        dfs(nums, 0, [], ans)
        return ans
