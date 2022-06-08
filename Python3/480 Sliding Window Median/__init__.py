import heapq
from heapq import heappush, heappop
from typing import List

import heapq
from heapq import heappush, heappop


class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        min_heap = []
        max_heap = []  # store negative numbers

        # if k is odd, max_heap have more numbers than minheap

        def rebalence():
            nonlocal min_heap, max_heap
            if len(max_heap) > len(min_heap) + 1:
                heappush(min_heap, -heappop(max_heap))
            if len(min_heap) > len(max_heap):
                heappush(max_heap, -heappop(min_heap))

        def delete_num(heap, n):
            idx = heap.index(n)
            heap[idx] = heap[-1]
            heap.pop()
            if idx < len(heap):
                heapq._siftup(heap, idx)
                heapq._siftdown(heap, 0, idx)

        ans = [0.0] * (len(nums) - k + 1)
        i = 0
        while i < len(nums):
            num = nums[i]
            if len(max_heap) == 0 or num <= -max_heap[0]:
                heappush(max_heap, -num)
            else:
                heappush(min_heap, num)
            rebalence()

            if i >= k:
                out_num = nums[i - k]
                if out_num <= -max_heap[0]:
                    delete_num(max_heap, -out_num)
                else:
                    delete_num(min_heap, out_num)
                rebalence()

            if i >= k - 1:
                if k % 2 == 0:
                    ans[i - k + 1] = min_heap[0] / 2.0 - max_heap[0] / 2.0
                else:
                    ans[i - k + 1] = -max_heap[0] / 1.0
            i += 1

        return ans


if __name__ == "__main__":
    sol = Solution()
    # result = sol.medianSlidingWindow([1, 2, -1, 3, 5], 2)
    # print("Sliding window medians are: " + str(result))
    result = sol.medianSlidingWindow([1, 2, -1, 3, 5], 3)
    print("Sliding window medians are: " + str(result))
