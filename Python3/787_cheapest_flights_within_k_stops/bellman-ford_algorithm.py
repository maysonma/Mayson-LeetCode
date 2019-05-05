class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        INT_MAX = int(1e9)
        dp = [INT_MAX] * n
        dp[src] = 0
        for i in range(K + 1):
            tmp = dp.copy()
            for u, v, w in flights:
                tmp[v] = min(tmp[v], dp[u] + w)
            dp = tmp
        return dp[dst] if dp[dst] < INT_MAX else -1
