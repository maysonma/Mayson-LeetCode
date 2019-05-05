class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        # Bellman-Ford's algorithm
        INT_MAX = int(1e9)
        dp = [INT_MAX] * (N + 1)
        dp[K] = 0
        for i in range(N - 1):
            changed = False
            tmp = dp.copy()
            for u, v, w in times:
                if dp[u] + w < tmp[v]:
                    tmp[v] = dp[u] + w
                    changed = True
            dp = tmp
            if not changed:
                break
        ans = max(dp[1:])
        return ans if ans < INT_MAX else -1
