from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if target >= letters[-1]:
            return letters[0]

        start = 0
        end = len(letters) - 1
        while start <= end:
            mid = start + (end - start) // 2
            if target >= letters[mid]:
                start = mid + 1
            else:
                end = mid - 1
        return letters[start]
