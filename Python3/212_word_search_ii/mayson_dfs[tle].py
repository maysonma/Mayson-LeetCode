class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m = len(board)
        n = len(board[0])

        def dfs(i, j, d, k):
            if i < 0 or i >= m or j < 0 or j >= n:
                return False
            if board[i][j] != words[k][d]:
                return False
            if d == len(words[k]) - 1:
                return True
            cur = board[i][j]
            board[i][j] = 0
            r = dfs(i - 1, j, d + 1, k) or dfs(i + 1, j, d + 1, k) or dfs(i, j - 1, d + 1, k) or dfs(i, j + 1, d + 1, k)
            board[i][j] = cur
            return r

        if m == 0:
            return []
        ans = []
        remain = list(range(len(words)))
        for i in range(m):
            for j in range(n):
                for k in remain:
                    if dfs(i, j, 0, k):
                        ans.append(words[k])
                        remain.remove(k)
        return sorted(ans)
