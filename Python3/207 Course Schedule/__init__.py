from collections import deque

# Breath-first Search
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        vertices = numCourses
        graph = {i: [] for i in range(vertices)}
        in_degrees = {i: 0 for i in range(vertices)}
        for v, u in prerequisites:
            graph[u].append(v)
            in_degrees[v] += 1

        sorted_order = []
        sources = deque()
        for v, d in in_degrees.items():
            if d == 0:
                sources.append(v)

        # sorting
        while sources:
            source = sources.popleft()
            sorted_order.append(source)
            for v in graph[source]:
                in_degrees[v] -= 1
                if in_degrees[v] == 0:
                    sources.append(v)

        return len(sorted_order) == vertices
