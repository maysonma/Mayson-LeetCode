from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        if n == 1:
            return matrix[0][0]
        start = matrix[0][0]
        end = matrix[n - 1][n - 1]
        while start < end:
            mid = start + (end - start) / 2
            # count #nums <= mid
            count = 0
            smaller = matrix[0][0]
            larger = matrix[n - 1][n - 1]
            col, row = 0, n - 1
            while col < n and row >= 0:
                if matrix[row][col] > mid:
                    larger = min(larger, matrix[row][col])
                    row -= 1
                else:  # matrix[row][col] <= mid
                    smaller = max(smaller, matrix[row][col])
                    count += row + 1
                    col += 1
            if count == k:
                return smaller
            elif count < k:
                start = larger
            else:  # count > k:
                end = smaller
        return start
