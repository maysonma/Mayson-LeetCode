from heapq import *


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        graph = collections.defaultdict(list)
        INT_MAX = int(1e9)
        for u, v, w in flights:
            graph[u].append((v, w))
        best = {}
        pq = [(0, 0, src)]
        while pq:
            cost, k, u = heappop(pq)
            if cost > best.get((k, u), INT_MAX): continue
            if u == dst: return cost
            for v, w in graph[u]:
                newcost = cost + w
                if newcost < best.get((k + 1, v), INT_MAX) and k < K + 1:
                    heappush(pq, (newcost, k + 1, v))
                    best[k + 1, v] = newcost
        return -1
