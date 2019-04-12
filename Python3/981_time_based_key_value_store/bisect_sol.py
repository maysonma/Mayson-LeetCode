import collections
import bisect


class TimeMap:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._dict = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self._dict[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        arr = self._dict[key]
        idx = bisect.bisect_right(arr, (timestamp, '{'))
        return "" if idx == 0 else arr[idx - 1][1]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
