class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(candidates, s, tar, cur, ans):
            candidates.sort()
            if tar == 0:
                ans.append(cur[:])
                return
            for i in range(s, len(candidates)):
                if candidates[i] > tar:
                    break
                cur.append(candidates[i])
                dfs(candidates, i, tar - candidates[i], cur, ans)
                cur.pop()

        ans = []
        dfs(candidates, 0, target, [], ans)
        return ans
