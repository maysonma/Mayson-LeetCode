class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        # 0 = uncolored, 1 = red, -1 = blue
        color = [0] * n

        def dfs(v, c):
            if color[v] != 0:
                if color[v] == c:
                    return True
                else:
                    return False
            color[v] = c
            for u in graph[v]:
                if not dfs(u, -c):
                    return False
            return True

        for i in range(n):
            if color[i] == 0:
                if not dfs(i, 1):
                    return False
        return True
