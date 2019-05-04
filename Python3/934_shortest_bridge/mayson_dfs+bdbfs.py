class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        m = len(A)
        n = len(A[0])
        dirn = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        s1 = set([])
        s2 = set([])
        s = [s1, s2]

        def valid(i, j):
            return 0 <= i < m and 0 <= j < n

        counter = 0

        def dfs(node, A):
            nonlocal s1, s2
            i, j = node
            if not valid(i, j) or A[i][j] != 1:
                return False
            A[i][j] = 2
            s[counter].add((i, j))
            for di, dj in dirn:
                dfs((i + di, j + dj), A)
            return True

        for i in range(m):
            for j in range(n):
                if dfs((i, j), A):
                    counter += 1

        step = -1
        while len(s1) > 0 and len(s2) > 0:
            step += 1
            if len(s1) > len(s2):
                s1, s2 = s2, s1
            s = set([])
            for node in s1:
                i, j = node
                for di, dj in dirn:
                    newi, newj = i + di, j + dj
                    if not valid(newi, newj):
                        continue
                    if (newi, newj) in s2:
                        return step
                    if A[newi][newj] != 0:
                        continue
                    A[newi][newj] = 1
                    s.add((newi, newj))
            s1 = s
        return -1
