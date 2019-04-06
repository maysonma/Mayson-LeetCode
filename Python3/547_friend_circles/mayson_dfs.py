from typing import *


class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        n = len(M)
        visited = [0] * n

        def dfs(i):
            if visited[i]:
                return False
            visited[i] = 1
            for j in range(n):
                if M[i][j] == 1:
                    dfs(j)
            return True

        counter = 0
        for i in range(n):
            if dfs(i):
                counter += 1
        return counter
