from sortedcontainers import SortedList


class SORTracker:
    def __init__(self):
        self.sorted_list = SortedList()
        self.i = 0

    def add(self, name: str, score: int) -> None:
        self.sorted_list.add((-score, name))

    def get(self) -> str:
        ans = self.sorted_list[self.i][1]
        self.i += 1
        return ans
