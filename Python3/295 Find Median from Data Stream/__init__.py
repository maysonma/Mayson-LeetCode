from heapq import heappush, heappop


class MedianFinder:
    def __init__(self):
        self.min_heap = []
        self.max_heap = []  # store negative numbers
        # max_heap to have more numbers if total number is odd

    def addNum(self, num: int) -> None:
        if len(self.max_heap) == 0 or num <= -self.max_heap[0]:
            heappush(self.max_heap, -num)
        else:
            heappush(self.min_heap, num)

        # balance
        if len(self.max_heap) > len(self.min_heap) + 1:
            heappush(self.min_heap, -heappop(self.max_heap))
        if len(self.min_heap) > len(self.max_heap):
            heappush(self.max_heap, -heappop(self.min_heap))

    def findMedian(self) -> float:
        if len(self.max_heap) == len(self.min_heap):
            return -self.max_heap[0] / 2.0 + self.min_heap[0] / 2.0
        else:
            return -self.max_heap[0]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
