from collections import deque
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        vertices = numCourses
        graph = {i: [] for i in range(vertices)}
        in_degrees = {i: 0 for i in range(vertices)}
        for v, u in prerequisites:
            graph[u].append(v)
            in_degrees[v] += 1

        sources = deque()
        for v, d in in_degrees.items():
            if d == 0:
                sources.append(v)

        sorted_order = []
        # sorting
        while sources:
            u = sources.popleft()
            sorted_order.append(u)
            for v in graph[u]:
                in_degrees[v] -= 1
                if in_degrees[v] == 0:
                    sources.append(v)

        if len(sorted_order) == vertices:
            return sorted_order
        else:
            return []
