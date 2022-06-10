from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(m, n, s, t, curr, ans):
            if m == n:
                ans.append(''.join(curr))
                return
            if s > 0:
                curr.append('(')
                dfs(m + 1, n, s - 1, t + 1, curr, ans)
                curr.pop()
            if t > 0:
                curr.append(')')
                dfs(m + 1, n, s, t - 1, curr, ans)
                curr.pop()

        ans = []
        dfs(0, 2 * n, n, 0, [], ans)
        return ans
