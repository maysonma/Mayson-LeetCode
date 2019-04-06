from typing import *


class UnionFind:
    def __init__(self, grid):
        m, n = len(grid), len(grid[0])
        self.count = 0
        self.parent = [-1] * (m * n)
        self.rank = [0] * (m * n)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    self.parent[i * n + j] = i * n + j
                    self.count += 1

    def find(self, i):
        # path compression
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, x, y):
        # union by rank
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx != rooty:
            if self.rank[rootx] > self.rank[rooty]:
                self.parent[rooty] = rootx
            elif self.rank[rootx] < self.rank[rooty]:
                self.parent[rootx] = rooty
            else:
                self.parent[rooty] = rootx
                self.rank[rootx] += 1
            self.count -= 1


class Solution:
    def numIslands(self, grid):
        if not grid or not grid[0]:
            return 0
        uf = UnionFind(grid)
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        m, n = len(grid), len(grid[0])

        def is_valid(i, j):
            nonlocal m, n
            if i < 0 or j < 0 or i >= m or j >= n:
                return False
            return True

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    for d in directions:
                        nr, nc = i + d[0], j + d[1]
                        if is_valid(nr, nc) and grid[nr][nc] == '1':
                            uf.union(i * n + j, nr * n + nc)
        return uf.count
