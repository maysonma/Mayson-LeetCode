from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        merged = []
        i = 0
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            # Before
            merged.append(intervals[i])
            i += 1

        start = newInterval[0]
        end = newInterval[1]
        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            # Merging
            start = min(start, intervals[i][0])
            end = max(end, intervals[i][1])
            i += 1

        merged.append([start, end])

        while i < len(intervals):
            # After
            merged.append(intervals[i])
            i += 1

        return merged
