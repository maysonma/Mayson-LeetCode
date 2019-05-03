from collections import defaultdict


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(defaultdict)
        ans = []
        # A / B = k -> g[a][b] = k
        for i in range(len(equations)):
            a, b = equations[i]
            graph[a][b] = values[i]
            graph[b][a] = 1 / values[i]

        def divide(a, b, visit) -> float:
            if a == b:
                return 1.0
            visit.add(a)
            for c in graph[a].keys():
                if c in visit:
                    continue
                r = divide(c, b, visit)
                if r < 0:
                    continue
                else:
                    return r * graph[a][c]
            return -1.0

        for q in queries:
            a, b = q
            if a not in graph or b not in graph:
                ans.append(-1.0)
            else:
                visit = set([])
                ans.append(divide(a, b, visit))
        return ans
