class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        states = [0] * n  # 0 = unknown, 1 = visiting, 2 = unsafe, 3 = safe

        def dfs(node):
            if states[node] != 0:
                return states[node]
            states[node] = 1
            for v in graph[node]:
                r = dfs(v)
                if r == 1 or r == 2:
                    states[node] = 2
                    return 2
            states[node] = 3
            return 3

        ans = []
        for v in range(n):
            if dfs(v) == 3:
                ans.append(v)
        return ans
