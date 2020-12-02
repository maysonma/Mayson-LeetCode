# class Solution:
#     def longestCommonSubsequence(self, text1: str, text2: str) -> int:
#         m = len(text1)
#         n = len(text2)
#         if m * n == 0: return 0
#         dp = [[0] * (n + 1) for _ in range(m + 1)]
#         for i in range(m + 1):
#             for j in range(n + 1):
#                 if i * j == 0:
#                     dp[i][j] = 0
#                 elif text1[i - 1] == text2[j - 1]:
#                     dp[i][j] = 1 + dp[i - 1][j - 1]
#                 else:
#                     dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
#         return dp[m][n]
#
#
# if __name__ == "__main__":
#     sol = Solution()
#     x = "AATTCCCCGACTGCAATTCACGCACC"
#     y = "GGCTTTTATTCTCCCTGTAAGT"
#
#     l = sol.longestCommonSubsequence(x, y)
#     print("L(X,Y)={}".format(l))


class Solution:
    @staticmethod
    def lcs(text1: str, text2: str):
        m = len(text1)
        n = len(text2)
        if m * n == 0: return 0
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            for j in range(n + 1):
                if i * j == 0:
                    dp[i][j] = 0
                elif text1[i - 1] == text2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

        lcs = []
        i, j = m, n
        while dp[i][j] != 0:
            if text1[i - 1] == text2[j - 1]:
                lcs.append(text1[i - 1])
                i, j = i - 1, j - 1
            elif dp[i - 1][j] >= dp[i][j - 1]:
                i -= 1
            else:
                j -= 1
        lcs = ''.join(reversed(lcs))
        return lcs

    @staticmethod
    def edit_distance(word1: str, word2: str):
        m = len(word1)
        n = len(word2)
        if m * n == 0: return max(m, n)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            for j in range(n + 1):
                if i * j == 0:
                    dp[i][j] = max(i, j)
                elif word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j],
                                       dp[i][j - 1],
                                       dp[i - 1][j - 1])
        return dp[m][n]

    @staticmethod
    def alignment_distance(text1: str, text2: str):
        m = len(text1)
        n = len(text2)
        if m * n == 0: return 3 * (m + n)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            for j in range(n + 1):
                if i * j == 0:
                    dp[i][j] = 3 * (i + j)
                elif text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] - 2
                else:
                    dp[i][j] = min(dp[i - 1][j - 1] + 1,
                                   dp[i - 1][j] + 3, dp[i][j - 1] + 3)
        return dp[m][n]


if __name__ == "__main__":
    x = "AATTCCCCGACTGCAATTCACGCACC"
    y = "GGCTTTTATTCTCCCTGTAAGT"

    lcs = Solution.lcs(x, y)
    d = Solution.edit_distance(x, y)
    a = Solution.alignment_distance(x, y)
    print(lcs)
    print("L(X,Y)={}\nD(X,Y)={}\nA(X,Y)={}\n".format(len(lcs), d, a))
