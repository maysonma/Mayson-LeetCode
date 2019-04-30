class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])

        def arr(x):
            q, r = divmod(x, n)
            return matrix[q][r]

        def bin_search(target, l, r):
            while l != r:
                m = l + (r - l) // 2
                if arr(m) == target:
                    return True
                elif arr(m) > target:
                    r = m
                else:
                    l = m + 1
            return False

        return bin_search(target, 0, m * n)
