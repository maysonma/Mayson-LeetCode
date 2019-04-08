class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, s, cur, ans):
            ans.append(cur[:])
            for i in range(s, len(nums)):
                cur.append(nums[i])
                dfs(nums, i + 1, cur, ans)
                cur.pop()

        ans = []
        dfs(nums, 0, [], ans)
        return ans
