from typing import *


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(candidates, s, tar, cur, ans):
            if tar == 0:
                ans.append(cur[:])
                return
            elif tar < 0:
                return
            for i in range(s, len(candidates)):
                cur.append(candidates[i])
                dfs(candidates, i, tar - candidates[i], cur, ans)
                cur.pop()

        ans = []
        dfs(candidates, 0, target, [], ans)
        return ans
