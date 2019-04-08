class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        def dfs(candidates, tar, s, cur, ans):
            if tar == 0:
                ans.append(tuple(cur[:]))
            for i in range(s, len(candidates)):
                if candidates[i] > tar:
                    break
                if i > s and candidates[i] == candidates[i - 1]:
                    continue
                cur.append(candidates[i])
                dfs(candidates, tar - candidates[i], i + 1, cur, ans)
                cur.pop()

        ans = []
        dfs(candidates, target, 0, [], ans)
        return ans
