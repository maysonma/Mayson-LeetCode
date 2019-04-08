class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        def dfs(candidates, tar, s, cur, ans):
            if tar == 0:
                ans.add(tuple(cur[:]))
            for i in range(s, len(candidates)):
                if candidates[i] > tar:
                    break
                cur.append(candidates[i])
                dfs(candidates, tar - candidates[i], i + 1, cur, ans)
                cur.pop()

        ans = set([])
        dfs(candidates, target, 0, [], ans)
        return list(map(list, ans))
