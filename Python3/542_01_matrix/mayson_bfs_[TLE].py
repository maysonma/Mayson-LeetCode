class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)
        if not m:
            return []
        n = len(matrix[0])
        if not n:
            return []
        MAX = m + n
        dist = [[MAX] * n for i in range(m)]
        dirn = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def bfs(x, y):
            d = -1
            cur_q = [(x, y)]
            while cur_q:
                d += 1
                nxt_q = []
                for i, j in cur_q:
                    if d > dist[i][j]:
                        continue
                    if matrix[i][j] == 0 and d > 0:
                        continue
                    dist[i][j] = d
                    for di, dj in dirn:
                        if 0 <= i + di < m and 0 <= j + dj < n:
                            nxt_q.append((i + di, j + dj))
                cur_q = nxt_q

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    bfs(i, j)
        return dist
