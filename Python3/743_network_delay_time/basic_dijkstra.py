class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        INT_MAX = int(1e9)
        dist = {u: INT_MAX for u in range(1, N + 1)}
        visited = [0] * (N + 1)
        dist[K] = 0
        while True:
            candidate_node = 0
            candidate_dist = INT_MAX
            for i in range(1, N + 1):
                if not visited[i] and dist[i] < candidate_dist:
                    candidate_dist = dist[i]
                    candidate_node = i
            if candidate_node == 0: break
            visited[candidate_node] = True
            for v, d in graph[candidate_node]:
                dist[v] = min(dist[v], dist[candidate_node] + d)
        ans = max(dist.values())
        return ans if ans < INT_MAX else -1
