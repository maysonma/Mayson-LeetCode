from heapq import *
from typing import List


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        max_heap = []
        for i in range(min(k, len(nums1))):
            for j in range(min(k, len(nums2))):
                n1 = nums1[i]
                n2 = nums2[j]
                if len(max_heap) < k:
                    heappush(max_heap, (-n1 - n2, i, j))
                else:
                    if n1 + n2 < -max_heap[0][0]:
                        heapreplace(max_heap, (-n1 - n2, i, j))
                    else:
                        break
        ans = [[nums1[i], nums2[j]] for _, i, j in max_heap]
        return ans
