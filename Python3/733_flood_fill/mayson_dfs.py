from typing import *


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        origin = image[sr][sc]
        new = newColor
        if origin == new:
            return image
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        m = len(image)
        n = len(image[0])

        def is_valid(x, y):
            if x >= 0 and x < m and y >= 0 and y < n:
                return True
            else:
                return False

        def dfs(i, j):
            nonlocal origin, new
            if image[i][j] != origin:
                return
            image[i][j] = new
            for dx, dy in directions:
                if is_valid(i + dx, j + dy):
                    dfs(i + dx, j + dy)

        dfs(sr, sc)
        return image
