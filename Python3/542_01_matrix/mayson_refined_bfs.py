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
        qs = [[(i, j)] for i in range(m) for j in range(n) if matrix[i][j] == 0]
        d = -1
        while qs:
            nxt_qs = []
            d += 1
            for idx, cur_q in enumerate(qs):
                nxt_q = []
                for i, j in cur_q:
                    if d >= dist[i][j]:
                        continue
                    dist[i][j] = d
                    for di, dj in dirn:
                        if 0 <= i + di < m and 0 <= j + dj < n:
                            nxt_q.append((i + di, j + dj))
                if nxt_q:
                    nxt_qs.append(nxt_q)
            qs = nxt_qs
        return dist
