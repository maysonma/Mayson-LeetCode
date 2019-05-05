class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        n = N
        graph = [[] for i in range(n)]
        for u, v in dislikes:
            graph[u - 1].append(v - 1)
            graph[v - 1].append(u - 1)

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
