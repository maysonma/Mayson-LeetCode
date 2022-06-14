class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
        mat = [[-1] * (n + 1) for _ in range(m + 1)]

        # base case
        for i in range(1, m + 1):
            mat[i][0] = 0
            mat[i][1] = i
        for j in range(1, n + 1):
            mat[0][j] = 0
            mat[1][j] = j
        for i in range(1, min(m, n) + 1):
            mat[i][i] = 1

        for i in range(2, m + 1):
            for j in range(2, n + 1):
                ans = []
                if i == j:
                    continue
                if i < j:
                    for k in range(1, i + 1):
                        ans.append(1 + mat[i - k][k] + mat[i][j - k])
                        # ans.append(1 + mat[i-k][j] + mat[k][j-k])
                else:
                    for k in range(1, j + 1):
                        ans.append(1 + mat[k][j - k] + mat[i - k][j])
                        # ans.append(1 + mat[i][j-k] + mat[i-k][k])
                mat[i][j] = min(ans)

        return mat[m][n]
