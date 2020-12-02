from typing import List


class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        n = len(edges) + 1
        if n == 0: return 0
        graph = [[] for _ in range(n)]
        for edge in edges:
            u, v = edge
            graph[u].append(v)
            graph[v].append(u)
        heights = [0] * n
        parents = [-1] * n
        diameter = -1

        def dfs(u):
            nonlocal diameter
            for v in graph[u]:
                if parents[u] == v: continue
                parents[v] = u
                dfs(v)

            h1 = h2 = -1
            for v in graph[u]:
                if parents[u] == v: continue
                if heights[v] > h1:
                    h1, h2 = heights[v], h1
                elif heights[v] > h2:
                    h2 = heights[v]
                else:
                    pass

            heights[u] = max(h1, h2) + 1
            diameter = max(diameter, h1 + h2 + 2)

        dfs(0)
        return diameter
