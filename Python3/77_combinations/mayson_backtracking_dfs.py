class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if k > n:
            return []

        def dfs(n, d, k, s, cur, ans):
            if d == k:
                ans.append(cur[:])
                return
            for i in range(s, n + 1):
                cur.append(i)
                dfs(n, d + 1, k, i + 1, cur, ans)
                cur.pop()

        ans = []
        dfs(n, 0, k, 1, [], ans)
        return ans
