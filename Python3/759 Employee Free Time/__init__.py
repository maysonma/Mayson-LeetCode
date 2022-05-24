# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end


from heapq import heappush, heappop


class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        class HeapItem:
            def __init__(self, interval, ee_id, j=0):
                self.ee_id = ee_id
                self.interval = interval
                self.j = j

            def __lt__(self, other):
                return self.interval.start < other.interval.start

        ans = []
        intervals = []
        for i, s in enumerate(schedule):
            heappush(intervals, HeapItem(s[0], i))

        last_end = float('-inf')
        while len(intervals) > 0:
            next_item = heappop(intervals)
            interval = next_item.interval
            ee_id = next_item.ee_id
            j = next_item.j

            if interval.start > last_end:
                ans.append(Interval(last_end, interval.start))
            if j + 1 < len(schedule[ee_id]):
                heappush(intervals, HeapItem(schedule[ee_id][j + 1], ee_id, j + 1))
            last_end = max(last_end, interval.end)

        return ans[1:]
