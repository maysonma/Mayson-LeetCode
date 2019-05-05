class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        n = N
        graph = [[] for i in range(n)]
        for u, v in dislikes:
            graph[u - 1].append(v - 1)
            graph[v - 1].append(u - 1)
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
