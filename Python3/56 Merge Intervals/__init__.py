from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) < 2:
            return intervals

        merged = []
        intervals.sort(key=lambda x: x[0])
        start = intervals[0][0]
        end = intervals[0][1]

        for interval in intervals[1:]:
            if interval[0] <= end:  # overlap
                end = max(end, interval[1])
            else:
                merged.append([start, end])
                start, end = interval
        merged.append([start, end])

        return merged
