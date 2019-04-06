from typing import *


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        counter = 0
        if grid is None or len(grid) == 0 or len(grid[0]) == 0:
            return 0
        m = len(grid)
        n = len(grid[0])

        def dfs(i, j):
            if grid[i][j] == '0':
                return
            else:
                grid[i][j] = '0'
                if i >= 1:
                    dfs(i - 1, j)
                if i < m - 1:
                    dfs(i + 1, j)
                if j >= 1:
                    dfs(i, j - 1)
                if j < n - 1:
                    dfs(i, j + 1)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    counter += 1
                    dfs(i, j)
        return counter

if __name__ == "__main__":
    input0 = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
    input1 = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
    s = Solution()
    print(s.numIslands(input1))