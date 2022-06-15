from collections import defaultdict
from heapq import *


class FreqStack:
    def __init__(self):
        self.freq_dict = defaultdict(int)
        self.max_heap = []
        self.seq_num = 0

    def push(self, val: int) -> None:
        self.freq_dict[val] += 1
        self.seq_num += 1
        temp = (-self.freq_dict[val], -self.seq_num, val)
        heappush(self.max_heap, temp)

    def pop(self) -> int:
        temp = heappop(self.max_heap)
        self.freq_dict[temp[2]] -= 1
        return temp[2]

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
