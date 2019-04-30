class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])

        def dfs(i, j, d):
            if i < 0 or i == m or j < 0 or j == n:
                return False
            if board[i][j] != word[d]:
                return False
            if d == len(word) - 1:
                return True
            curr = board[i][j]
            board[i][j] = 0
            r = dfs(i - 1, j, d + 1) or dfs(i + 1, j, d + 1) or dfs(i, j - 1, d + 1) or dfs(i, j + 1, d + 1)
            board[i][j] = curr
            return r

        if m == 0:
            return False
        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        return False
