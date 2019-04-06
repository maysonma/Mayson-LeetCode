from typing import *


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        m = len(grid)
        n = len(grid[0])
        max_so_far = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def is_valid(i, j):
            nonlocal m, n
            if 0 <= i < m and 0 <= j < n:
                return True
            else:
                return False

        def dfs(i, j):
            if grid[i][j] == 0:
                return 0
            else:
                grid[i][j] = 0
                counter = 1
                nonlocal directions
                for dx, dy in directions:
                    if is_valid(i + dx, j + dy):
                        counter += dfs(i + dx, j + dy)
                return counter

        for i in range(m):
            for j in range(n):
                max_so_far = max(max_so_far, dfs(i, j))
        return max_so_far
