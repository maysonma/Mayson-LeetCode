import collections


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
        l = 0
        r = len(arr)
        while l != r:
            m = l + (r - l) // 2
            if arr[m][0] > timestamp:
                r = m
            else:
                l = m + 1
        if l == 0:
            return ""
        else:
            return arr[l - 1][1]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
