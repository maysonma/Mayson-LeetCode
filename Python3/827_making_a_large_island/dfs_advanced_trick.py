from typing import *


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        m = len(grid)
        n = len(grid[0])
        color = 2
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        color_area_dict = {0: 0}
        max_area = 0

        def area_dfs(i, j):
            nonlocal m, n, color, directions, grid
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != 1:
                return 0
            grid[i][j] = color
            a = 1
            for di, dj in directions:
                a += area_dfs(i + di, j + dj)
            return a

        for i in range(m):
            for j in range(n):
                area = area_dfs(i, j)
                if area > 0:
                    color_area_dict[color] = area
                    max_area = max(area, max_area)
                    color += 1

        def get_color(i, j):
            if i < 0 or i >= m or j < 0 or j >= n:
                return 0
            else:
                return grid[i][j]

        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                    continue
                color_set = {get_color(i + di, j + dj) for di, dj in directions}
                max_area = max(max_area, 1 + sum([color_area_dict[color] for color in color_set]))
        return max_area
