from typing import List


class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        n = len(edges) + 1
        graph = [[] for _ in range(n)]
        for edge in edges:
            u, v = edge
            graph[u].append(v)
            graph[v].append(u)

        distance = [-1] * n
        distance[0] = 0
        q = [0]
        while len(q) != 0:
            u = q.pop(0)
            for v in graph[u]:
                if distance[v] != -1: continue
                distance[v] = distance[u] + 1
                q.append(v)

        farmost = dis = 0
        for i, d in enumerate(distance):
            if d > dis: farmost, dis = i, d

        distance = [-1] * n
        distance[farmost] = 0
        q = [farmost]
        while len(q) != 0:
            u = q.pop(0)
            for v in graph[u]:
                if distance[v] != -1: continue
                distance[v] = distance[u] + 1
                q.append(v)

        return max(distance)
