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
        # BFS
        q = [(i, j) for i in range(m) for j in range(n) if matrix[i][j] == 0]
        d = -1
        while q:
            nxt_q = []
            d += 1
            for i, j in q:
                if d >= dist[i][j]:
                    continue
                dist[i][j] = d
                for di, dj in dirn:
                    if 0 <= i + di < m and 0 <= j + dj < n:
                        nxt_q.append((i + di, j + dj))
            q = nxt_q
        return dist
