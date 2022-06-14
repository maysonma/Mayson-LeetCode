from heapq import *
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def eu_dist_to_origin_squared(p):
            return p[0] ** 2 + p[1] ** 2

        max_heap = [(-eu_dist_to_origin_squared(points[i]), i) for i in range(k)]
        heapify(max_heap)

        for i in range(k, len(points)):
            d = eu_dist_to_origin_squared(points[i])
            if d < -max_heap[0][0]:
                heapreplace(max_heap, (-d, i))

        ans = [points[i] for _, i in max_heap]
        return ans
