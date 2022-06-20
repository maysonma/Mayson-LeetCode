from collections import deque
from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        degrees = {i: 0 for i in range(n)}
        graph = {i: [] for i in range(n)}
        for u, v in edges:
            degrees[u] += 1
            degrees[v] += 1
            graph[u].append(v)
            graph[v].append(u)

        leaves = deque()
        for u, d in degrees.items():
            if d == 1:
                leaves.append(u)

        total_nodes = n
        while total_nodes > 2:
            curr_level = len(leaves)
            total_nodes -= curr_level
            for _ in range(curr_level):
                u = leaves.popleft()
                for v in graph[u]:
                    degrees[v] -= 1
                    if degrees[v] == 1:
                        leaves.append(v)

        return list(leaves)
