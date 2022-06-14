from collections import defaultdict
from heapq import *


class Solution:
    def reorganizeString(self, s: str) -> str:
        freq_dict = defaultdict(int)
        for char in s:
            freq_dict[char] += 1

        max_heap = [(-f, char) for char, f in freq_dict.items()]
        heapify(max_heap)
        ans = []

        frequency = 0
        char = 'c'
        while max_heap:
            temp = heappop(max_heap)
            ans.append(temp[1])
            if frequency > 0:
                heappush(max_heap, (-frequency, char))
            frequency, char = -temp[0] - 1, temp[1]

        if len(ans) < len(s):
            return ""
        else:
            return ''.join(ans)
