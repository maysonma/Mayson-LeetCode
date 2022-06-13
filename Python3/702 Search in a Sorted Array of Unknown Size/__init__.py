# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
# class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader: 'ArrayReader', target: int) -> int:
        start, end = 0, 1
        while reader.get(end) < target:  # double the range
            new_start = end + 1
            end = new_start + (end - start + 1) * 2
            start = new_start

        while start <= end:
            mid = start + (end - start) // 2
            if reader.get(mid) == target:
                return mid
            elif target < reader.get(mid):
                end = mid - 1
            else:
                start = mid + 1

        return -1
