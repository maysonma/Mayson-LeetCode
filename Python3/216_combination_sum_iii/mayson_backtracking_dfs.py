class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def dfs(m, target, s, cur, ans):
            if m == k:
                if target == 0:
                    ans.append(cur[:])
                return
            for i in range(s, 10):
                if target < i:
                    return
                cur.append(i)
                dfs(m + 1, target - i, i + 1, cur, ans)
                cur.pop()

        ans = []
        dfs(0, n, 1, [], ans)
        return ans
