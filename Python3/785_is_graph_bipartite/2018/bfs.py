from typing import List


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        # 0 = uncolored, 1 = red, -1 = blue
        color = [0] * n

        def bfs(cur_q, c):
            while cur_q:
                nxt_q = []
                for u in cur_q:
                    for v in graph[u]:
                        if color[v] == color[u]:
                            return False
                        if color[v] == 0:
                            color[v] = c
                            nxt_q.append(v)
                cur_q = nxt_q
                c = -c
            return True

        for i in range(n):
            if color[i] == 0:
                color[i] = 1
                if not bfs([i], -1):
                    return False
        return True
