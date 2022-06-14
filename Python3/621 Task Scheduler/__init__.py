from heapq import *
from collections import defaultdict, deque
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq_dict = defaultdict(int)
        for t in tasks:
            freq_dict[t] += 1

        max_heap = [(-f, t) for t, f in freq_dict.items()]
        heapify(max_heap)

        queue = deque()
        time = 0
        while max_heap or queue:
            if not max_heap:
                time = queue[0][2]
            else:
                f_neg, t = heappop(max_heap)
                time += 1
                if f_neg < -1:
                    queue.append((-f_neg - 1, t, time + n))
            while queue and queue[0][2] == time:
                temp = queue.popleft()
                heappush(max_heap, (-temp[0], temp[1]))
        return time
