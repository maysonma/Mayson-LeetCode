from collections import defaultdict, deque
from heapq import *


class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        if k <= 1:
            return s

        freq_dict = defaultdict(int)
        for char in s:
            freq_dict[char] += 1

        max_heap = [(-f, char) for char, f in freq_dict.items()]
        heapify(max_heap)
        queue = deque()

        ans = []

        while max_heap:
            f_neg, char = heappop(max_heap)
            ans.append(char)
            queue.append((-f_neg - 1, char))
            if len(queue) == k:
                previous_freq, previous_char = queue.popleft()
                if previous_freq > 0:
                    heappush(max_heap, (-previous_freq, previous_char))

        if len(ans) == len(s):
            return ''.join(ans)
        else:
            return ""
