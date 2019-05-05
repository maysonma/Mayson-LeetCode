from collections import defaultdict


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        graph = defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))
        q = [(src, 0)]
        step = -1
        INT_MAX = 2 ** 30
        cur_max = INT_MAX
        while q:
            step += 1
            if step == K + 2:
                break
            nq = []
            for u, cur in q:
                if u == dst:
                    cur_max = min(cur, cur_max)
                    continue
                for v, w in graph[u]:
                    if cur + w > cur_max: continue
                    nq.append((v, cur + w))
            q = nq
        return cur_max if cur_max < INT_MAX else -1
