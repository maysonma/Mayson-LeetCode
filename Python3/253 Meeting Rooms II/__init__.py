from typing import List

from heapq import heappop, heappush


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        min_rooms = 0
        ends = []
        for interval in intervals:
            while len(ends) > 0 and ends[0] <= interval[0]:
                heappop(ends)
            heappush(ends, interval[1])
            min_rooms = max(min_rooms, len(ends))
        return min_rooms


if __name__ == "__main__":
    s = Solution()
    print(s.minMeetingRooms(
        [[4, 18], [1, 35], [12, 45], [25, 46], [22, 27]]
    ))
