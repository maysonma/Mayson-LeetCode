class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        dp = [[-1] * n for _ in range(m)]
        def l(i, j):
            if i < 0 or j < 0:
                return 0
            if dp[i][j] < 0:
                if text1[i] == text2[j]:
                    dp[i][j] = l(i-1, j-1) + 1
                else:
                    dp[i][j] = max(l(i-1, j), l(i, j-1))
            return dp[i][j]
        return l(m-1, n-1)