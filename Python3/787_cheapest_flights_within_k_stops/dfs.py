from collections import defaultdict


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        graph = defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))
        visited = [0] * n
        INT_MAX = 2 ** 30
        cur_max = INT_MAX

        def dfs(u, dst, k, visited, cur):
            nonlocal cur_max
            if u == dst:
                cur_max = cur
                return
            if k == 0:
                return
            for v, w in graph[u]:
                if visited[v]: continue
                if cur + w > cur_max: continue
                visited[v] = 1
                dfs(v, dst, k - 1, visited, cur + w)
                visited[v] = 0

        dfs(src, dst, K + 1, visited, 0)
        return cur_max if cur_max < INT_MAX else -1
