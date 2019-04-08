from collections import deque
from typing import *


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        n = len(digits)
        digit_char_arr = [['a', 'b', 'c'],
                          ['d', 'e', 'f'],
                          ['g', 'h', 'i'],
                          ['j', 'k', 'l'],
                          ['m', 'n', 'o'],
                          ['p', 'q', 'r', 's'],
                          ['t', 'u', 'v'],
                          ['w', 'x', 'y', 'z']]
        q = deque([[]])
        ans = []

        def bfs(q):
            nonlocal n, ans, digits, digit_char_arr
            while q:
                fringe = q.popleft()
                m = len(fringe)
                if m == n:
                    ans.append(''.join(fringe))
                    continue
                for char in digit_char_arr[ord(digits[m]) - ord('2')]:
                    q.append(fringe[:] + [char])

        bfs(q)
        return ans
