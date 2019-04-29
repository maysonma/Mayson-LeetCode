class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        if n == 0:
            return []
        visit = [0] * n  # 0 = unknown, 1 = visiting, 2 = visited
        ans = []

        def dfs(node):
            if visit[node] == 1:
                return False
            if visit[node] == 2:
                return True
            visit[node] = 1
            for v in graph[node]:
                if not dfs(v):
                    return False
            visit[node] = 2
            ans.append(node)
            return True

        for v in range(n):
            dfs(v)
        return sorted(ans)
