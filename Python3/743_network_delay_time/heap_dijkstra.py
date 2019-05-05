class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        pq = [(0, K)]
        dist = {}
        while pq:
            d, u = heapq.heappop(pq)
            if u in dist:
                continue
            else:
                dist[u] = d
            for v, d2 in graph[u]:
                if v in dist:
                    continue
                else:
                    heapq.heappush(pq, (d + d2, v))
        return max(dist.values()) if len(dist) == N else -1
